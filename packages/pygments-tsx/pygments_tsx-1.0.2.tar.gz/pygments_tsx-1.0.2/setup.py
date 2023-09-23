from setuptools import setup

# import os
# import datetime


# # Get the version from the git tag, and write to VERSION.
# ref = None
# if "GITHUB_REF" in os.environ:
#     ref = os.environ["GITHUB_REF"]

# if ref and ref is not None and ref.startswith("refs/tags/"):
#     version = ref.replace("refs/tags/", "")
# else:
#     version = datetime.datetime.now().strftime("%Y.%m.%d%H%M%S")

# print(version)

# requirements = []
# with open('requirements.txt') as f:
#     requirements = f.read().splitlines()

setup(
    # name='pygments_tsx',
    # version=version,
    package_dir={"": "src"},
    packages=['pygments_tsx'],
    entry_points="""
        [pygments.lexers]
        jsx=jsx:JsxLexer
        tsx=pygments_tsx.tsx:TypeScriptXLexer
    """,
    # install_requires=requirements
    )
