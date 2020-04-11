# Zernit's downstream for ion

This directory is dedicated to defining backend for [ion](https://github.com/redox-os/ion) downstream logic


### Blockers
ION shell is currently not officially supported due to these reasons:
- No linting
  - How do we enforce code quality?
- Not POSIX Compliant
  - How do we make it work on POSIX?
  - Possible fork?
- Lacks gitpod support <https://github.com/gitpod-io/gitpod/issues/1389>
  - This is minor, but annoyance and it has highlighting support for vim
- Does not support windows

### Where to get support
- Chat: https://chat.redox-os.org/redox/channels/ion
- Docummentation: https://doc.redox-os.org/ion-manual/html/