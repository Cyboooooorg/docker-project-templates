[![DPT Logo](./assets/pictures/dpt-logo.png)](https://github.com/Cyboooooorg/docker-project-templates)

# Docker Project Templates

<div align="center" markdown="1">

[![GitHub repo license](https://img.shields.io/github/license/Cyboooooorg/docker-project-templates?style=flat&logo=github&logoColor=whitesmoke&label=License)](https://www.gnu.org/licenses/gpl-3.0.fr.html)&#160;
[![GitHub repo forks](https://img.shields.io/github/forks/Cyboooooorg/docker-project-templates?style=flat&logo=github&logoColor=whitesmoke&label=Forks)](https://github.com/Cyboooooorg/docker-project-templates/network)&#160;
[![GitHub repo stars](https://img.shields.io/github/stars/Cyboooooorg/docker-project-templates?style=flat&logo=github&logoColor=whitesmoke&label=Stars)](https://github.com/Cyboooooorg/docker-project-templates/stargazers)&#160;
[![GitHub repo contributors](https://img.shields.io/github/contributors-anon/Cyboooooorg/docker-project-templates?style=flat&logo=github&logoColor=whitesmoke&label=Contributors)](https://github.com/Cyboooooorg/docker-project-templates/graphs/contributors)&#160;
[![GitHub repo size](https://img.shields.io/github/repo-size/Cyboooooorg/docker-project-templates?style=flat&logo=github&logoColor=whitesmoke&label=Repo%20Size)](https://github.com/Cyboooooorg/docker-project-templates/archive/refs/heads/main.zip)

</div>

## Quick Introduction

This repository contains a set of templates for Docker projects. It is intended to be used as a starting point for new projects.

## Table of Contents

- [Quick Introduction](#quick-introduction)
- [Table of Contents](#table-of-contents)
- [Project Description](#project-description)
  - [Available Templates](#available-templates)
  - [How to Use](#how-to-use)
  - [How to Contribute](#how-to-contribute)

## Project Description

<div align="center" markdown="1">

[![GitHub repo last commit](https://img.shields.io/github/last-commit/Cyboooooorg/docker-project-templates?style=flat&logo=github&logoColor=whitesmoke&label=Last%20Commit)](https://github.com/Cyboooooorg/docker-project-templates/graphs/commit-activity)&#160;
[![GitHub repo issues](https://img.shields.io/github/issues/Cyboooooorg/docker-project-templates?style=flat&logo=github&logoColor=whitesmoke&label=Issues)](https://github.com/Cyboooooorg/docker-project-templates/issues)&#160;
[![GitHub repo pull requests](https://img.shields.io/github/issues-pr/Cyboooooorg/docker-project-templates?style=flat&logo=github&logoColor=whitesmoke&label=Pull%20Requests)](https://github.com/Cyboooooorg/docker-project-templates/pulls)

</div>

Since Docker is a very powerful tool, it is often used in many projects. However, it is not always easy to start a new project with Docker. This repository aims to provide a set of templates for Docker projects. It is intended to be used as a starting point for new projects.

It is important to note that these templates are not intended to be used as is. They are only intended to be used as a starting point for new projects. Indeed, each project is different and requires different tools. Therefore, it is important to adapt the templates to the needs of each project.

This repository provides templates for many languages and tools. However, it is not possible to provide templates for all languages and tools. Therefore, if you want to add a template for a language or tool that is not yet available, please feel free to contribute to this repository.

### Available Templates

- [Databases](./templates/databases)
  - [MySQL](./templates/databases/mysql)
- [Python](./templates/python)
  - [Native](./templates/python/native)
- [More to come...](./templates)

### How to Use

To use these templates, you must first clone this repository. Then, you must copy the template you want to use to the root of your project. Finally, you must adapt the template to your project.

Install [Task](https://taskfile.dev/installation/) and run the following command to see the available tasks:

```bash
task
```

Or go in any template folder and run the following command to see the available tasks:

```bash
task
```

If this the first time you use the template, you must run the following command to initialize the template:

```bash
task init
```

Then, you can run the following command to start the project:

```bash
task docker:build docker:up
```

### How to Contribute

If you want to contribute to this repository, you can do so by creating a pull request. However, before creating a pull request, please make sure that your contribution is relevant and that it does not break anything.
