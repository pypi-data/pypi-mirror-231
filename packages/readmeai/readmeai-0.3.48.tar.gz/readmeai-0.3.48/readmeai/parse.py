"""Methods to parse and extract dependency file metadata."""

import json
import re
from typing import Callable, Dict, List, Union

import toml
import yaml

from . import logger

logger = logger.Logger(__name__)


# Precompiled regular expressions for performance
GO_MOD_REGEX = re.compile(r"^\s*([\w\.\-_/]+)\s+v[\w\.\-_/]+")
GRADLE_REGEX = re.compile(r'implementation\([\'"]([^\'"]+):[^\'"]+[\'"]\)')
CMAKE_REGEX = re.compile(r"add_executable\([^)]+\s+([^)]+)\)")
CONFIGURE_AC_REGEX = re.compile(r"AC_CHECK_LIB\([^)]+\s+([^)]+)\)")
MAKEFILE_AM_REGEX = re.compile(r"bin_PROGRAMS\s*=\s*(.+)")
MAVEN_REGEX = re.compile(
    r"<dependency>\s*<groupId>([^<]+)</groupId>\s*<artifactId>([^<]+)</artifactId>\s*<version>([^<]+)</version>"
)


def handle_parse_error(error_type: str, excinfo: Exception):
    """Handles exceptions raised during parsing."""
    logger.error(f"Error parsing {error_type}: {str(excinfo)}")


def load_content(
    content: str, loader: Callable, error_type: str, key: str = None
) -> Union[Dict, List]:
    """Loads content into a data structure."""
    try:
        data = loader(content)
        if key and isinstance(data, dict) and key in data:
            return data[key]
        return data
    except Exception as excinfo:
        handle_parse_error(error_type, excinfo)
        return []


def parse_yaml_file(content: str, key: str) -> List[str]:
    """Parses a YAML file and returns a list of package names."""
    data = load_content(content, yaml.safe_load, "YAML file", key)
    return list(data.keys()) if isinstance(data, dict) else []


def parse_json_file(content: str, keys: List[str] = None) -> List[str]:
    """Parses a JSON file and returns a list of package names."""
    data = load_content(content, json.loads, "JSON file")
    package_names = []
    if keys and isinstance(data, dict):
        for key in keys:
            if key in data:
                package_names.extend(data[key].keys())
    return package_names


def parse_toml_file(content: str, keys: List[str] = None) -> List[str]:
    """Parses a TOML file and returns a list of package names."""
    data = load_content(content, toml.loads, "TOML file")
    package_names = []
    if keys and isinstance(data, dict):
        for key_path in keys:
            sub_data = data
            for k in key_path.split("."):
                sub_data = sub_data.get(k, {})
            if isinstance(sub_data, dict):
                package_names.extend(sub_data.keys())
    return package_names


def parse_with_regex(content: str, regex: re.Pattern) -> List[str]:
    """Parses file using regex and returns list of package names."""
    return regex.findall(content)


def parse_docker_compose(content: str) -> List[str]:
    """Parses docker-compose.yml and returns list of service names."""
    return parse_yaml_file(content, "services")


def parse_conda_env_file(content: str) -> List[str]:
    """Parses conda env file and returns list of package names."""
    # Additional logic specific to conda env files
    data = parse_yaml_file(content, "dependencies")
    dependencies = []
    for package in data:
        if isinstance(package, str):
            dependencies.append(package.split("=")[0])
        elif isinstance(package, dict):
            dependencies.extend(package.keys())
    return dependencies


def parse_pipfile(content: str) -> List[str]:
    """Parses Pipfile and returns list of package names."""
    return parse_toml_file(content, keys=["packages", "dev-packages"])


def parse_pipfile_lock(content: str) -> List[str]:
    """Parses Pipfile.lock and returns list of package names."""
    return parse_json_file(content, keys=["default", "develop"])


def parse_poetry_lock(content: str) -> List[str]:
    """Parses poetry.lock and returns list of package names."""
    # Additional logic specific to poetry.lock files
    sections = content.split("[[package]]")
    packages = []
    for section in sections[1:]:
        lines = section.strip().splitlines()
        for line in lines:
            if line.startswith("name = "):
                package_name = line.split('"')[1]
                packages.append(package_name)
                break
    return packages


def parse_pyproject_toml(content: str) -> List[str]:
    """Parses pyproject.toml and returns list of package names."""
    return parse_toml_file(
        content, keys=["tool.poetry.dependencies", "tool.poetry.optional-dependencies"]
    )


def parse_requirements_file(content: str) -> List[str]:
    """Parses requirements.txt and returns list of package names."""
    return parse_with_regex(content, GO_MOD_REGEX)


def parse_cargo_toml(content: str) -> List[str]:
    """Parses Cargo.toml and returns list of package names."""
    return parse_with_regex(content, GO_MOD_REGEX)


def parse_cargo_lock(content: str) -> List[str]:
    """Parses Cargo.lock and returns list of package names."""
    return parse_toml_file(content, keys=["package"])


def parse_package_json(content: str) -> List[str]:
    """Parses package.json and returns list of package names."""
    return parse_json_file(
        content, keys=["dependencies", "devDependencies", "peerDependencies"]
    )


def parse_yarn_lock(content: str) -> List[str]:
    """Parses yarn.lock and returns list of package names."""
    return parse_with_regex(content, GO_MOD_REGEX)


def parse_package_lock_json(content: str) -> List[str]:
    """Parses package-lock.json and returns list of package names."""
    # Additional logic specific to package-lock.json files
    data = parse_json_file(content, keys=["dependencies"])
    return [package[7:] for package in data if package.startswith("@types/")]


def parse_go_mod(content: str) -> List[str]:
    """Parses go.mod and returns list of package names."""
    return parse_with_regex(content, GO_MOD_REGEX)


def parse_gradle(content: str) -> List[str]:
    """Parses build.gradle and returns list of package names."""
    return parse_with_regex(content, GRADLE_REGEX)


def parse_maven(content: str) -> List[str]:
    """Parses pom.xml and returns list of package names."""
    return parse_with_regex(content, MAVEN_REGEX)


def parse_cmake(content: str) -> List[str]:
    """Parses CMakeLists.txt and returns list of package names."""
    return parse_with_regex(content, CMAKE_REGEX)


def parse_configure_ac(content: str) -> List[str]:
    """Parses configure.ac and returns list of package names."""
    return parse_with_regex(content, CONFIGURE_AC_REGEX)


def parse_makefile_am(content: str) -> List[str]:
    """Parses Makefile.am and returns list of package names."""
    matches = parse_with_regex(content, MAKEFILE_AM_REGEX)
    package_names = []
    for match in matches:
        deps = filter(None, match.split())
        package_names.extend(deps)
    return package_names
