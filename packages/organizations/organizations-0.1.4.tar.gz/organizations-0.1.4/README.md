# Organizations App

## 1. Services

### Library

This app provides organizations management to your projects installing it on requirements.txt

## 2. Requirements

- Python 3.9
- You can install all the requirements with:

```bash
pip install -r requirements.txt
or
pip3 install -r requirements.txt
```

## 3. Deployment

This repo cannot deploy on its own. You need to add it to another project and call it.

### step-0

You need a project repository. Found it and clone.

```bash
git clone your_repository
```

This app needs to be in a .tar.gz format.

```bash
python -m build
```

### step-1

You need to replace this lib with previus ones. *To run it locally.*

Add previous .tar.gz and put it on a package folder.

```bash
# requirements.txt
package/organizations-0.1.14.tar.gz
```

```bash
# Dockerfile or Dockerfile.prod
ADD package/ /code/package
```

### step-2

Go to project readme to run it.

### 4. Content

You can find the following components.

- Organizations
- Organizations DIDs
- Organizations Keys
- Operators
- Operators Dids
- Issuers
- Intermediarys
- Onboarding Notifications (not working yet)
  