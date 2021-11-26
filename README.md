# README

## Commands

### Create SSH

```bash
ssh-keygen -t rsa -b 4096 -C "joe@example.com"
```

### Validate SSH

```bash
eval "$(ssh-agent -s)"
```

### Check SSH public key

```bash
cat ~/.ssh/id_rsa.pub
```
