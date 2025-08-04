export ANSIBLE_HOST_KEY_CHECKING=False
ansible-playbook -i localhost, -e ansible_user=$1 -e ansible_password=$2  -e ansible_become_password=$2 -e role_name=jenkins-config playbook.yaml -vv
