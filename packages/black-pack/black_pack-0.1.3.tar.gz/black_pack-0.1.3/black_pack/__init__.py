from .version import __version__
import os
import sys
import toml
import yaml
import glob
import pkg_resources
import subprocess
import numpy
import difflib
import dictdiffer
import restructuredtext_lint
import io
import shutil


def random_hash_16bit():
    return "{:04X}".format(int(numpy.random.uniform(low=1, high=2**16)))


def check_package(pkg_dir):
    expected_requires = []
    check_gitignore(pkg_dir=pkg_dir)
    check_project_toml(pkg_dir=pkg_dir, expected_requires=expected_requires)
    check_requirements_txt(
        pkg_dir=pkg_dir, expected_requires=expected_requires
    )
    check_all_python_files_are_black(pkg_dir=pkg_dir)
    license_key = check_license(pkg_dir=pkg_dir)
    pkg = check_setup_py(pkg_dir=pkg_dir)

    rmg = check_readme_rst(pkg_dir=pkg_dir)

    if "basename" in pkg:
        base_dir = os.path.join(pkg_dir, pkg["basename"])

        if not os.path.isdir(base_dir):
            print(
                "E-787E: directory ./{:s} is missing.".format(pkg["basename"])
            )

        potential_packages = make_list_of_potential_python_packages(
            pkg_dir=pkg_dir, base_dir=base_dir
        )

        if "packages" in pkg:
            for potential_package in potential_packages:
                if potential_package not in pkg["packages"]:
                    print(
                        "E-A878: "
                        "setup.py -> setup -> packages is missing "
                        "'{:s}'.".format(potential_package)
                    )

    if "basename" in pkg:
        pkg_dir_basename = os.path.basename(os.path.abspath(pkg_dir))
        if not pkg_dir_basename == pkg["basename"]:
            print(
                "E-2474: "
                "The basename of the path {:s} ".format(pkg_dir_basename)
                + "dose not match the basename {:s} ".format(pkg["basename"])
                + "in setup.py."
            )

    if "image_references" in rmg:
        if "basename" in pkg and "TestStatus" in rmg["image_references"]:
            """
            Example
            -------
            .. |TestStatus| image:: https://github.com/cherenkov-plenoscope/basename/actions/workflows/test.yml/badge.svg?branch=main
                :target: https://github.com/cherenkov-plenoscope/basename/actions/workflows/test.yml
            """
            if not rmg["image_references"]["TestStatus"]["image"].endswith(
                "{basename:s}/actions/workflows/test.yml/badge.svg?branch=main".format(
                    basename=pkg["basename"]
                )
            ):
                print(
                    "E-08F8: "
                    "README.rst -> |TestStatus| -> image-link: "
                    "does not match package-name "
                    "'{basename:s}' in setup.py.".format(
                        basename=pkg["basename"]
                    )
                )

            if not rmg["image_references"]["TestStatus"]["target"].endswith(
                "{basename:s}/actions/workflows/test.yml".format(
                    basename=pkg["basename"]
                )
            ):
                print(
                    "E-2F11: "
                    "README.rst -> |TestStatus| -> target-link: "
                    "does not match package-name "
                    "'{basename:s}' in setup.py.".format(
                        basename=pkg["basename"]
                    )
                )

        if "name" in pkg and "PyPiStatus" in rmg["image_references"]:
            """
            Example
            -------
            .. |PyPiStatus| image:: https://img.shields.io/pypi/v/name
                :target: https://pypi.org/project/name
            """
            if not rmg["image_references"]["PyPiStatus"]["image"].endswith(
                "https://img.shields.io/pypi/v/{name:s}".format(
                    name=pkg["name"]
                )
            ):
                print(
                    "E-2861: "
                    "README.rst -> |PyPiStatus| -> image-link: "
                    "does not match package-name '{name:s}' in setup.py.".format(
                        name=pkg["name"]
                    )
                )

            if not rmg["image_references"]["PyPiStatus"]["target"].endswith(
                "https://pypi.org/project/{name:s}".format(name=pkg["name"])
            ):
                print(
                    "E-0E7A: "
                    "README.rst -> |PyPiStatus| -> "
                    "target-link does not match package-name "
                    "'{name:s}' in setup.py.".format(name=pkg["name"])
                )

    ghg = check_github_workflows(pkg_dir=pkg_dir)
    if "name" in pkg:
        if "release" in ghg:
            if "jobs" in ghg["release"]:
                if "pypi-publish" in ghg["release"]["jobs"]:
                    if "environment" in ghg["release"]["jobs"]["pypi-publish"]:
                        if (
                            "url"
                            in ghg["release"]["jobs"]["pypi-publish"][
                                "environment"
                            ]
                        ):
                            release_url = ghg["release"]["jobs"][
                                "pypi-publish"
                            ]["environment"]["url"]

                            if not release_url.endswith(pkg["name"]):
                                print(
                                    "E-CA7B: "
                                    "./.github/workflows/release.yml -> "
                                    "jobs.pypi-publish.environment.url: "
                                    "does not end with '{:s}'.".format(
                                        pkg["name"]
                                    )
                                )

    # check for tests
    # ---------------
    if "basename" in pkg:
        tests_dir = os.path.join(pkg_dir, pkg["basename"], "tests")
        if not os.path.isdir(tests_dir):
            print(
                "E-3D08: "
                "./{:s}/tests ".format(pkg["basename"]) + "does not exist."
            )

        potential_test_files = glob.glob(os.path.join(tests_dir, "test*.py"))
        if not potential_test_files:
            print(
                "E-4E82: "
                "./{:s}/tests ".format(pkg["basename"])
                + "does not contain any test*.py file."
            )


def has_any_upper(s):
    for char in s:
        if str.isupper(char):
            return True
    return False


def read_text(path):
    with open(path, "rt") as f:
        txt = f.read()
    return txt


def read_yml(path):
    return yaml.safe_load(read_text(path=path))


def write_yml(path, a):
    with open(path, "wt") as f:
        f.write(yaml.safe_dump(a))


def tokenize_version_string_into_hex(v):
    vv = str.split(v, ".")
    vi = [int(_v, base=16) for _v in vv]
    return vi


def compare_hex_tokens_greater_equal(a, b):
    assert len(a) == len(b)

    if a[0] == b[0]:
        if len(a) == 1:
            return True
        else:
            return compare_hex_tokens_greater_equal(a[1:], b[1:])
    elif a[0] > b[0]:
        return True
    else:
        return False


def compare_version_string_greater_equal(a, b):
    aa = tokenize_version_string_into_hex(a)
    bb = tokenize_version_string_into_hex(b)

    max_num_tokens = max([len(aa), len(bb)])
    for i in range(max_num_tokens - len(aa)):
        aa.append(int("0", base=16))
    for i in range(max_num_tokens - len(bb)):
        bb.append(int("0", base=16))

    return compare_hex_tokens_greater_equal(aa, bb)


def check_project_toml(
    pkg_dir, expected_requires=[], expected_setuptools_minimal_version="42"
):
    if not os.path.isfile(os.path.join(pkg_dir, "project.toml")):
        print("E-5E2B: ./project.toml is missing.")
        return

    try:
        with open(os.path.join(pkg_dir, "project.toml"), "rt") as f:
            project = toml.loads(f.read())
    except toml.TomlDecodeError as err:
        print("E-F42A: ./project.toml bad syntax.")

    if "build-system" not in project:
        print("E-3F9E: ./project.toml has no 'build-system'.")
        return

    if "requires" in project["build-system"]:
        if len(project["build-system"]["requires"]) == 0:
            print(
                "E-749E: "
                "./project.toml[build-system][requires] "
                "is empty."
            )
        else:
            first_requirement = project["build-system"]["requires"][0]

            if "setuptools>=" not in first_requirement:
                print(
                    "E-522D: "
                    "./project.toml[build-system][requires][0] "
                    "has no 'setuptools>='."
                )
            else:
                actual_setuptools_minimal_version = str.strip(
                    first_requirement, "setuptools>="
                )

                if not compare_version_string_greater_equal(
                    actual_setuptools_minimal_version,
                    expected_setuptools_minimal_version,
                ):
                    print(
                        "E-C6F7: "
                        "./project.toml[build-system][requires][0] "
                        "expectec setuptools>={:s}.".format(
                            expected_setuptools_minimal_version
                        )
                    )

        for expected_require in expected_requires:
            if expected_require not in project["build-system"]["requires"]:
                print(
                    "E-EAF5: "
                    "./project.toml[build-system][requires] "
                    "has no '{:s}'.".format(expected_require)
                )

        for require in project["build-system"]["requires"]:
            if has_any_upper(require):
                print(
                    "E-1319: "
                    "./project.toml[build-system][requires] "
                    "has upper cases in package-name '{:s}'.".format(require)
                )

    else:
        print("E-8EB6: ./project.toml[build-system] has no 'requires'.")

    if "build-backend" in project["build-system"]:
        if "setuptools.build_meta" != project["build-system"]["build-backend"]:
            print(
                "E-E4DA: "
                "./project.toml[build-system][build-backend] "
                "is not 'setuptools.build_meta'."
            )
            return
    else:
        print("E-B9A8: ./project.toml[build-system] has no 'build-backend'.")


def check_requirements_txt(pkg_dir, expected_requires):
    if not os.path.isfile(os.path.join(pkg_dir, "requirements.txt")):
        print("E-2F45: ./requirements.txt is missing.")
        return

    txt = read_text(os.path.join(pkg_dir, "requirements.txt"))

    requires = str.splitlines(txt)

    for expected_require in expected_requires:
        if expected_require not in requires:
            print(
                "E-BCD8: ./requirements.txt has no '{:s}'.".format(
                    expected_require
                )
            )

    for require in requires:
        if has_any_upper(require):
            print(
                "E-E644: "
                "./requirements.txt "
                "has upper cases in package-name '{:s}'.".format(require)
            )


def check_license(pkg_dir):
    known_licenses = list_licences()

    if not os.path.isfile(os.path.join(pkg_dir, "LICENSE")):
        print("E-A0A1: ./LICENSE is missing.")
        return None

    txt = read_text(os.path.join(pkg_dir, "LICENSE"))

    first_line = str.splitlines(txt)[0]

    match = None
    license_keys = []
    for license_key in known_licenses:
        head = str.splitlines(known_licenses[license_key]["raw"])[0]
        if head == first_line:
            match = license_key
        license_keys.append(license_key)

    if not match:
        license_keys_str = str.join(", ", license_keys)
        print(
            "E-2A0C: ./LICENSE does not match any in [{:s}].".format(
                license_keys_str
            )
        )

    return match


def black_diff(path):
    p = subprocess.Popen(
        [
            "black",
            "--line-length",
            "79",
            "--target-version",
            "py37",
            "--diff",
            path,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    p.wait()
    o = p.stdout.read()
    return o


def is_pythoncode_black(path):
    diff = black_diff(path=path)
    if len(diff) > 0:
        return False
    return True


def is_restructuredtext_fine(path):
    messages = restructuredtext_lint.lint_file(path)
    if len(messages) > 0:
        return False
    return True


def list_licences():
    res_dir = pkg_resources.resource_filename("black_pack", "resources")
    licenses = {}
    licenses["GPLv3"] = {
        "pypi": (
            "License :: "
            "OSI Approved :: "
            "GNU General Public License v3 (GPLv3)"
        ),
        "github": "gpl-3.0",
        "raw": read_text(os.path.join(res_dir, "GPLv3.txt")),
    }
    licenses["MIT"] = {
        "pypi": "License :: OSI Approved :: MIT License",
        "github": "mit",
        "raw": read_text(os.path.join(res_dir, "MIT.txt")),
    }
    return licenses


def split_comma_with_bracket_balance(s):
    s = s.strip()
    if not s.endswith(","):
        s = s + ","

    parts_i = []

    b_bal = 0
    c_bal = 0
    p_bal = 0
    q_bal = True
    for i in range(len(s)):
        if s[i] == "[":
            b_bal += 1
        if s[i] == "]":
            b_bal -= 1

        if s[i] == "{":
            c_bal += 1
        if s[i] == "}":
            c_bal -= 1

        if s[i] == "(":
            c_bal += 1
        if s[i] == ")":
            c_bal -= 1

        if s[i] == '"':
            q_bal = not q_bal

        if (
            s[i] == ","
            and b_bal == 0
            and c_bal == 0
            and p_bal == 0
            and q_bal == True
        ):
            parts_i.append(i)

    out = []
    start = 0
    for stop in parts_i:
        part = s[start:stop]
        out.append(str(part))
        start = stop + 1

    return out


def parse_kwargs_of_python_function(s):
    raw_kwargs = split_comma_with_bracket_balance(s)
    for i in range(len(raw_kwargs)):
        raw_kwargs[i] = raw_kwargs[i].strip()

    kwargs = {}
    # print(raw_kwargs)
    for raw_kwarg in raw_kwargs:
        # print(raw_kwarg)
        assert "=" in raw_kwarg
        eqpos = raw_kwarg.find("=")
        key = raw_kwarg[0:eqpos]
        arg = raw_kwarg[eqpos + 1 :]
        kwargs[key] = arg
    return kwargs


def check_all_python_files_are_black(pkg_dir):
    allpaths = glob.glob(os.path.join(pkg_dir, "**"), recursive=True)

    pypaths = []
    for path in allpaths:
        if path.lower().endswith(".py"):
            pypaths.append(path)

    for pypath in pypaths:
        if not is_pythoncode_black(path=pypath):
            relpath = os.path.relpath(pypath, start=pkg_dir)
            print("E-58F1: {:s} is not 'black -l79 -tpy37'.".format(relpath))


def make_read_readme_code():
    return (
        'with open("README.rst", "r", encoding="utf-8") as f:\n'
        "    long_description = f.read()"
    )


def make_read_version_code():
    return (
        'with open(os.path.join("{name:s}", "version.py")) as f:\n'
        "    txt = f.read()\n"
        "    last_line = txt.splitlines()[-1]\n"
        "    version_string = last_line.split()[-1]\n"
        '    version = version_string.strip("\\"\'")'
    )


def check_setup_py(pkg_dir):
    pkg = {}

    if not os.path.isfile(os.path.join(pkg_dir, "setup.py")):
        print("E-A9A4: ./setup.py is missing.")
        return pkg

    if not is_pythoncode_black(os.path.join(pkg_dir, "setup.py")):
        print("E-530A: ./setup.py is not 'black -l79 -tpy37'.")

    txt = read_text(os.path.join(pkg_dir, "setup.py"))

    blocks = txt.split("\n\n")
    for i in range(len(blocks)):
        blocks[i] = blocks[i].strip()

    if "import setuptools" not in blocks[0]:
        print(
            "E-BFFB: ./setup.py expected 'import setuptools' in import-block."
        )

    if "import os" not in blocks[0]:
        print("E-07D6: ./setup.py expected 'import os' in import-block.")

    if make_read_readme_code() not in blocks[1]:
        print("E-9EB9: ./setup.py expected read-README-block.")

    last_block = blocks[-1]

    if last_block.startswith("setuptools.setup(") and last_block.endswith(")"):
        setup_kwargs = parse_kwargs_of_python_function(last_block[17:-1])

        if "name" in setup_kwargs:
            pkg["name"] = setup_kwargs["name"].strip('"')
        else:
            print("E-39F3: ./setup.py -> setup() has no 'name'.")

        if "version" in setup_kwargs:
            if "version" != setup_kwargs["version"]:
                print(
                    "E-8283: "
                    "./setup.py -> setup() "
                    "expected 'version=version' in order to use "
                    "the version-variable read in from version.py."
                )
        else:
            print("E-94C2: ./setup.py -> setup() has no 'version'.")

        if "description" not in setup_kwargs:
            print("E-B102: ./setup.py -> setup() has no 'description'.")

        if "long_description" in setup_kwargs:
            if "long_description" != setup_kwargs["long_description"]:
                print(
                    "E-E0B9: "
                    "./setup.py -> setup() "
                    "expected 'long_description=long_description' "
                    "in order to use the long_description-variable "
                    "read in from README.rst."
                )
        else:
            print("E-096D: ./setup.py -> setup() has no 'long_description'.")

        if "long_description_content_type" in setup_kwargs:
            if "text/x-rst" != setup_kwargs[
                "long_description_content_type"
            ].strip('"'):
                print(
                    "E-9E71: "
                    "./setup.py -> setup() "
                    'expected long_description_content_type="text/x-rst".'
                )
        else:
            print(
                "E-E2CE: "
                "./setup.py -> setup() "
                "has no 'long_description_content_type'."
            )

        if "url" in setup_kwargs:
            pkg["url"] = setup_kwargs["url"].strip('"')
        else:
            print("E-8456: ./setup.py -> setup() has no 'url'.")

        if "author" in setup_kwargs:
            pkg["author"] = setup_kwargs["author"].strip('"')
        else:
            print("E-7BDB: ./setup.py -> setup() has no 'author'.")

        if "author_email" in setup_kwargs:
            pkg["author_email"] = setup_kwargs["author_email"].strip('"')
        else:
            print("E-49E5: ./setup.py -> setup() has no 'author_email'.")

        if "packages" in setup_kwargs:
            try:
                pkg["packages"] = split_comma_with_bracket_balance(
                    s=setup_kwargs["packages"][1:-1]
                )
                for i in range(len(pkg["packages"])):
                    pkg["packages"][i] = pkg["packages"][i].strip(" ")
                    pkg["packages"][i] = pkg["packages"][i].strip('"')
            except:
                print("E-A9CC: ./setup.py -> setup() packages syntax.")
        else:
            print("E-6A2F: ./setup.py -> setup() has no 'packages'.")

        if "package_data" not in setup_kwargs:
            print("E-96F3: ./setup.py -> setup() has no 'package_data'.")

        if "install_requires" in setup_kwargs:
            try:
                pkg["install_requires"] = split_comma_with_bracket_balance(
                    s=setup_kwargs["install_requires"][1:-1]
                )
                for i in range(len(pkg["install_requires"])):
                    pkg["install_requires"][i] = pkg["install_requires"][
                        i
                    ].strip()
                    pkg["install_requires"][i] = pkg["install_requires"][
                        i
                    ].strip('"')
            except:
                print("E-CBEB: ./setup.py -> setup() install_requires syntax.")
        else:
            print("E-6B00: ./setup.py -> setup() has no 'install_requires'.")

        if "classifiers" in setup_kwargs:
            try:
                pkg["classifiers"] = split_comma_with_bracket_balance(
                    s=setup_kwargs["classifiers"][1:-1]
                )
                for i in range(len(pkg["classifiers"])):
                    pkg["classifiers"][i] = pkg["classifiers"][i].strip()
                    pkg["classifiers"][i] = pkg["classifiers"][i].strip('"')
            except:
                print("E-6C27: ./setup.py -> setup() classifiers syntax.")

            if "Programming Language :: Python :: 3" not in pkg["classifiers"]:
                print(
                    "E-20A7: "
                    "./setup.py -> setup() -> classifiers missing "
                    "'Programming Language :: Python :: 3'."
                )

            if "Natural Language :: English" not in pkg["classifiers"]:
                print(
                    "E-B98D: "
                    "./setup.py -> setup() -> classifiers "
                    "missing 'Natural Language :: English'."
                )

            if "Operating System :: OS Independent" not in pkg["classifiers"]:
                print(
                    "E-719A: "
                    "./setup.py -> setup() -> classifiers "
                    "missing 'Operating System :: OS Independent'."
                )

        else:
            print("E-9C4F: ./setup.py -> setup() has no 'classifiers'.")

        if "project_urls" in setup_kwargs and "url" in setup_kwargs:
            print(
                "W-C8B1: "
                "./setup.py -> setup() "
                "contains 'project_urls' what might not be needed "
                "becasue 'url' is also present."
            )

        if "license" in setup_kwargs and "url" in setup_kwargs:
            print(
                "W-915F: "
                "./setup.py -> setup() "
                "contains 'license'. Use classifiers instead."
            )

        # sanity checks in pkg
        pkg["basename"] = pkg["packages"][0]

        if not pkg["name"].startswith(pkg["basename"]):
            print(
                "E-8391: "
                "./setup.py -> setup() -> name "
                "does not start with name of packages[0]."
            )

        if not pkg["url"].endswith(pkg["basename"]):
            print(
                "E-EFBD: "
                "./setup.py -> setup() -> url "
                "does not end with name of packages[0]."
            )

        read_version_code = make_read_version_code().format(
            name=pkg["basename"]
        )
        if read_version_code not in blocks[2]:
            print("E-64A5: ./setup.py expected read-version-block.")

    else:
        print("E-47EC: ./setup.py expected last block to be setup-block.")

    return pkg


def folder_might_be_a_python_package(path):
    if os.path.isdir(path):
        if os.path.isfile(os.path.join(path, "__init__.py")):
            return True
    return False


def make_list_of_potential_python_package_paths(path, l=[]):
    if folder_might_be_a_python_package(path):
        l.append(path)
        for file in os.listdir(path):
            l = make_list_of_potential_python_package_paths(
                os.path.join(path, file), l=l
            )
    return l


def make_list_of_potential_python_packages(pkg_dir, base_dir):
    ppaths = make_list_of_potential_python_package_paths(path=base_dir)
    for i in range(len(ppaths)):
        ppaths[i] = os.path.relpath(path=ppaths[i], start=pkg_dir)

    potential_packages = []
    for i in range(len(ppaths)):
        package = ppaths[i].replace(os.path.sep, ".")
        if package != ".":
            potential_packages.append(package)
    return potential_packages


def check_readme_rst(pkg_dir):
    out = {}

    if not os.path.isfile(os.path.join(pkg_dir, "README.rst")):
        print("E-D308: ./README.rst is missing.")
        return out

    if not is_restructuredtext_fine(path=os.path.join(pkg_dir, "README.rst")):
        print("E-EF4B: ./README.rst -> Errors. Check 'rst-lint'.")

    txt = read_text(os.path.join(pkg_dir, "README.rst"))

    blocks = txt.split("\n\n")
    for i in range(len(blocks)):
        blocks[i] = blocks[i].strip()

    # title
    # -----
    title_block = blocks[0]
    title_lines = title_block.splitlines()
    h0 = "#" * len(title_lines[0]) == title_lines[0]
    h1 = len(title_lines[1]) == title_lines[0]
    h2 = "#" * len(title_lines[2]) == title_lines[0]
    if not h0 and h1 and h2:
        print("E-340C: ./README.rst -> title is not '###\\nABC\\n###\\n.'")

    title_batch_lines = title_block.splitlines()[3:]
    title_batch_str = str.join(" ", title_batch_lines)
    title_batches = title_batch_str.split(" ")
    for i in range(len(title_batches)):
        title_batches[i] = title_batches[i].strip()

    if len(title_batches) < 3:
        print(
            "E-8566: "
            "./README.rst -> batches -> Expected at least three batches."
        )
    else:
        if "|TestStatus|" not in title_batches[0]:
            print(
                "E-814E: "
                "./README.rst -> batches -> |TestStatus| is not 1st batch."
            )

        if "|PyPiStatus|" not in title_batches[1]:
            print(
                "E-DFF5: "
                "./README.rst -> batches -> |PyPiStatus| is not 2nd batch."
            )

        if "|BlackStyle|" not in title_batches[2]:
            print(
                "E-C619: "
                "./README.rst -> batches -> |BlackStyle| is not 3rd batch."
            )

    image_references = {}
    for block in blocks:
        try:
            ref = tokenize_restructured_text_image_reference(txt=block)
            key = ref.pop("key")
            image_references[key] = ref
        except BaseException as e:
            pass

    if "TestStatus" not in image_references:
        print(
            "E-1882: "
            "./README.rst -> batches -> "
            "|TestStatus| has no image-reference. No indent=4?"
        )

    if "PyPiStatus" not in image_references:
        print(
            "E-E431: "
            "./README.rst -> batches -> |PyPiStatus| "
            "has no image-reference. No indent=4?"
        )

    if "BlackStyle" not in image_references:
        print(
            "E-D6CB: "
            "./README.rst -> batches -> |BlackStyle| "
            "has no image-reference. No indent=4?"
        )
    else:
        black_image_link = (
            "https://img.shields.io/badge/code%20style-black-000000.svg"
        )
        if not image_references["BlackStyle"]["image"] == black_image_link:
            print(
                "E-E59F: "
                "./README.rst -> batches -> |BlackStyle| "
                "image-link shpuld be: {:s}.".format(black_image_link)
            )

        black_target_link = "https://github.com/psf/black"
        if not image_references["BlackStyle"]["target"] == black_target_link:
            print(
                "E-0EB8: "
                "./README.rst -> batches -> |BlackStyle| "
                "target-link shpuld be: {:s}.".format(black_target_link)
            )

    out["image_references"] = image_references
    out["blocks"] = blocks

    return out


def tokenize_restructured_text_image_reference(txt):
    """
    Example:
    .. |BlackStyle| image:: https://img.shields.io/badge/code%20style-black-000000.svg
        :target: https://github.com/psf/black
    """
    s = txt.strip()
    out = {}
    tokens = s.split(" ")
    assert tokens[0] == ".."
    assert tokens[1].startswith("|")
    assert tokens[1].endswith("|")
    out["key"] = tokens[1].strip("|")
    assert tokens[2].endswith("image::")
    out["image"] = tokens[3].strip()
    assert tokens[7] == ":target:"
    out["target"] = tokens[8]
    return out


def check_github_workflows(pkg_dir):
    github_dir = os.path.join(pkg_dir, ".github")
    out = {}

    if not os.path.isdir(github_dir):
        print("E-1BBF: ./.github directory is missing.")
        return out

    workflows_dir = os.path.join(github_dir, "workflows")
    if not os.path.isdir(workflows_dir):
        print("E-C6E7: ./.github/workflows directory is missing.")
        return out

    test_yml_path = os.path.join(workflows_dir, "test.yml")
    if not os.path.isfile(test_yml_path):
        print("E-DEFC: ./.github/workflows/test.yml is missing.")
        return out
    else:
        out["test"] = read_yml(path=test_yml_path)
        check_github_workflows_test(test_yml=out["test"])

    release_yml_path = os.path.join(workflows_dir, "release.yml")
    if not os.path.isfile(release_yml_path):
        print("E-134E: ./.github/workflows/release.yml is missing.")
        return out
    else:
        out["release"] = read_yml(path=release_yml_path)
        check_github_workflows_release(release_yml=out["release"])

    return out


def check_gitignore(pkg_dir):
    gitignore_path = os.path.join(pkg_dir, ".gitignore")

    if not os.path.isfile(gitignore_path):
        print("E-930D: ./.gitignore file is missing.")
        return

    res_dir = pkg_resources.resource_filename("black_pack", "resources")
    exp_filename = "gitignore_commit_8e67b94_2023-09-10"
    exp_path = os.path.join(res_dir, exp_filename)

    with open(exp_path) as ff:
        fromlines = ff.readlines()
    with open(gitignore_path) as tf:
        tolines = tf.readlines()

    diff = difflib.context_diff(fromlines, tolines)

    try:
        _ = diff.__next__()
        print("E-1564: ./.gitignore differs from {:s}.".format(exp_path))
    except StopIteration:
        pass


def check_github_workflows_test(test_yml):
    res_dir = pkg_resources.resource_filename("black_pack", "resources")

    expected_test_yml = read_yml(
        path=os.path.join(res_dir, "github_workflows_test.yml")
    )

    diff = dictdiffer.diff(first=expected_test_yml, second=test_yml)

    try:
        diff.__next__()
        print("E-A3CF: ./.github/workflows/test.yml is not as expected.")
    except StopIteration:
        pass


def check_github_workflows_release(release_yml):
    res_dir = pkg_resources.resource_filename("black_pack", "resources")

    expected_release_yml = read_yml(
        path=os.path.join(res_dir, "github_workflows_release.yml")
    )

    diff = dictdiffer.diff(first=expected_release_yml, second=release_yml)
    diffs = [dd for dd in diff]

    if len(diffs) == 0:
        print(
            "E-671E: "
            "./.github/workflows/release.yml -> "
            "jobs.pypi-publish.environment.url: Must not be 'NAME'."
        )
        return

    if len(diffs) > 1:
        print(
            "E-671E: "
            "./.github/workflows/release.yml "
            "is too different from {:s}.".format(expected_release_yml)
        )
        return

    ch = diffs[0]
    if len(ch) != 3:
        if "change" != ch[0]:
            if "jobs.pypi-publish.environment.url" != ch[1]:
                print(
                    "E-671E: "
                    "./.github/workflows/release.yml -> "
                    "jobs.pypi-publish.environment.url "
                    "is not set."
                )
                return

    return


def make_restructured_text_image_reference(key, image, target):
    return ".. |{key:s}| image:: {image:s}\n    :target: {target:s}\n".format(
        key=key,
        image=image,
        target=target,
    )


def make_default_readme_rst(name, basename, github_organization_url):
    ss = io.StringIO()
    ss.write(len(basename) * "#")
    ss.write("\n")
    ss.write(basename)
    ss.write("\n")
    ss.write(len(basename) * "#")
    ss.write("\n")
    ss.write("|TestStatus| |PyPiStatus| |BlackStyle|\n")
    ss.write("\n")
    ss.write("Lorem ipsum...\n")
    ss.write("\n")
    ss.write(
        make_restructured_text_image_reference(
            key="TestStatus",
            image=os.path.join(
                github_organization_url,
                basename,
                "actions/workflows/test.yml/badge.svg?branch=main",
            ),
            target=os.path.join(
                github_organization_url, basename, "actions/workflows/test.yml"
            ),
        )
    )
    ss.write("\n")
    ss.write(
        make_restructured_text_image_reference(
            key="PyPiStatus",
            image="https://img.shields.io/pypi/v/{:s}".format(name),
            target="https://pypi.org/project/{:s}".format(name),
        )
    )
    ss.write("\n")
    ss.write(
        make_restructured_text_image_reference(
            key="BlackStyle",
            image="https://img.shields.io/badge/code%20style-black-000000.svg",
            target="https://github.com/psf/black",
        )
    )
    ss.write("\n")
    ss.seek(0)
    return ss.read()


def make_setup_py(
    name,
    basename,
    author,
    url_base,
    pypi_license_classifier,
):
    s = ""
    s += "import setuptools\n"
    s += "import os\n"
    s += "\n"
    s += "\n"
    s += make_read_readme_code()
    s += "\n"
    s += "\n"
    s += make_read_version_code().format(name=basename)
    s += "\n"
    s += "\n"
    s += "setuptools.setup(\n"
    s += "    name={:s},\n".format(name)
    s += "    version=version,\n"
    s += '    description=("This is {:s}."),\n'.format(basename)
    s += "    long_description=long_description,\n"
    s += '    long_description_content_type="text/x-rst",\n'
    s += '    url="{:s}",\n'.format(os.path.join(url_base, basename))
    s += '    author="{:s}",\n'.format(author)
    s += '    author_email="{:s}@mail",\n'.format(author)
    s += "    packages=[\n"
    s += '        "{:s}",\n'.format(basename)
    s += "    ],\n"
    s += '    package_data={{"{:s}": []}},\n'.format(basename)
    s += "    install_requires=[],\n"
    s += "    classifiers=[\n"
    s += '        "Programming Language :: Python :: 3",\n'
    s += '        "{:s}",\n'.format(pypi_license_classifier)
    s += '        "Operating System :: OS Independent",\n'
    s += '        "Natural Language :: English",\n'
    s += "    ],\n"
    s += ")\n"
    return s


def init(
    pkg_dir,
    name="my_package",
    basename="my_package",
    author="AUTHOR",
    exist_ok=True,
    github_organization_url="https://github.com/my-organization/",
    github_workflows_test=True,
    github_workflows_release=True,
    license_key="MIT",
):
    resources_dir = pkg_resources.resource_filename("black_pack", "resources")

    known_licenses = list_licences()
    if license_key not in known_licenses:
        print("No template for license {:s}.".format(license_key))
        return

    # main directories
    # ================
    os.makedirs(pkg_dir, exist_ok=exist_ok)
    os.makedirs(os.path.join(pkg_dir, name), exist_ok=exist_ok)
    with open(os.path.join(pkg_dir, name, "version.py"), "wt") as f:
        f.write('__version__ = "0.0.0"\n')

    with open(os.path.join(pkg_dir, name, "__init__.py"), "wt") as f:
        f.write("from .version import __version__\n")

    os.makedirs(os.path.join(pkg_dir, name, "tests"), exist_ok=exist_ok)
    with open(
        os.path.join(pkg_dir, name, "tests", "test_import.py"), "wt"
    ) as f:
        f.write(
            "import {:s}\n".format(basename)
            + "\n"
            + "\n"
            + "def test_import():\n"
            + "    pass\n"
        )

    with open(os.path.join(pkg_dir, "setup.py"), "wt") as f:
        setup_py_str = make_setup_py(
            name=name,
            basename=basename,
            author=author,
            url_base=github_organization_url,
            pypi_license_classifier=known_licenses[license_key]["pypi"],
        )
        f.write(setup_py_str)

    shutil.copy(
        src=os.path.join(resources_dir, "requirements.txt"),
        dst=os.path.join(pkg_dir, "requirements.txt"),
    )

    shutil.copy(
        src=os.path.join(resources_dir, "project.toml"),
        dst=os.path.join(pkg_dir, "project.toml"),
    )

    shutil.copy(
        src=os.path.join(resources_dir, "gitignore_commit_8e67b94_2023-09-10"),
        dst=os.path.join(pkg_dir, ".gitignore"),
    )

    with open(os.path.join(pkg_dir, "README.rst"), "wt") as f:
        f.write(
            make_default_readme_rst(
                name=name,
                basename=basename,
                github_organization_url=github_organization_url,
            )
        )

    with open(os.path.join(pkg_dir, "LICENSE"), "wt") as f:
        f.write(known_licenses[license_key]["raw"])

    # github workflows
    # ================
    if github_workflows_test or github_workflows_release:
        os.makedirs(
            os.path.join(pkg_dir, ".github", "workflows"), exist_ok=exist_ok
        )

    if github_workflows_test:
        shutil.copy(
            src=os.path.join(resources_dir, "github_workflows_test.yml"),
            dst=os.path.join(pkg_dir, ".github", "workflows", "test.yml"),
        )

    if github_workflows_release:
        release_yml = read_yml(
            path=os.path.join(resources_dir, "github_workflows_release.yml")
        )
        release_yml["jobs"]["pypi-publish"]["environment"][
            "url"
        ] = "https://pypi.org/project/{:s}".format(name)
        write_yml(
            path=os.path.join(pkg_dir, ".github", "workflows", "release.yml"),
            a=release_yml,
        )
