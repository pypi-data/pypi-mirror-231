# VerMa

Version Manager. CLI tool to help you manage your package versioning.

## Install

Use `pip` to install the package from Pypi:

```sh
pip install verma
```

## Using the CLI tool

After installing Verma, `verma` command will be enabled in your CLI. This command has a subcommand `bump` that can be used to bump the current version that can be read from the last _git tag_ that it finds in the repo. You can pass parameters to `bump` subcommand, such as:

- `-p, --patch-pattern`: The **regex** pattern to be searched in the last commit to bump the _patch_ version.
- `-m, --minor-pattern`: The **regex** pattern to be searched in the last commit to bump the _minor_ version.
- `-M, --major-pattern`: The **regex** pattern to be searched in the last commit to bump the _major_ version.

Some examples using `verma bump [OPTIONS]`:

```sh
verma bump -p "(fix):" -m "(feat):" -M "BREAKING CHANGES!:"
verma bump --patch-pattern "(fix):" --minor-pattern "(feat):" --major-pattern "BREAKING CHANGES!:"
```

You can pass multiple patterns for each version level:

```sh
verma bump -p "(fix):" -m "(feat):" -p "fix:" -m "feat:" -M "BREAKING CHANGES!:"
```

> Verma will bump the version level of the highest version level's pattern that was matched in last commit.
