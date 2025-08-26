# Install angular app
```
npm install -g @angular/cli
ng new hello-world-app
cd hello-world-app
ng serve

```
will open at https://localhost:4200

### Install firebase tools
```
npm install -g firebase-tools

```
### Create firebase token for deployment
```
firebase login:ci

```

### deploy using token
```
ng build --prod
firebase deploy --token "$FIREBASE_TOKEN"

```