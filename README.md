# Python template repository

[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://black.readthedocs.io/en/stable/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![ci](https://github.com/iancleary/new-component/workflows/ci/badge.svg)](https://github.com/iancleary/new-component/actions/workflows/ci.yml)

Ian Cleary ([iancleary](https://github.com/iancleary))

## Description

**Welcome!** This is a CLI for creating [styled-components] for React projects quickly.

## Quickstart

```sh
❯ pipx install new-component
❯ new-component --help
```

That will output the following:

```sh
Usage: new_component [OPTIONS] NAME

  Creates an new component directory in a React project, with opinionated
  defaults for styled-components.

  See https://styled-components.com/ for more information.

Arguments:
  NAME  Name of component to create.  [required]

Options:
  -d, --directory TEXT  The directory in which to create the component.
                        [default: src/components/]
  -v, --version         Show the application's version and exit.
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.
  --help                Show this message and exit.
```

## Example Usage

The first and only arguement is the name of the component to create.

```bash
new-component ContactForm
```

This will create:

`src/components/index.js`
`src/components/ContactForm.js`

The contents of the files will be as follows:

```js
// `src/components/index.js`
export { default } from "./ContactForm"
```

```js
// `src/components/ContactForm.js`
import React from "react"
import styled from "styled-components"

const ContactForm = ({ children }) => {
  return <Wrapper>{children}</Wrapper>
}

const Wrapper = styled.div`
  /* CSS Goes Here */
`

export default ContactForm
```

## Further information

See [CONTRIBUTING.md](.github/CONTRIBUTING.md).
