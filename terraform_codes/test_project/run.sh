if [ "$1" == "apply" ]; then
    echo "terraform initializing"
    terraform init -backend-config=env-dev/state.tfvars
    echo "terraform plan"
    terraform plan -var-file=env-dev/main.tfvars
    echo "terraform apply"
    terraform apply -var-file=env-dev/main.tfvars -auto-approve
elif [ "$1" == "destroy" ]; then
    echo "terraform destroy"
    terraform destroy -var-file=env-dev/main.tfvars -auto-approve
else
    echo "Usage: $0 {apply|destroy}"
fi
