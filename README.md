# friendly-guacamole

???

## development

```
$ cp hosts.example hosts
$ vim hosts # and change the dev-vm IP
$ ansible-playbook -i hosts playbook-dev.yml
```

## ???production??? usage

in theory,

```
$ ansible-pull -K -U https://github.com/canine-systems/friendly-guacamole.git
```
