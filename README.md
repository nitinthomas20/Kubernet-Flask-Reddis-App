# Flask + Redis on Kubernetes (with Minikube)

This project demonstrates how to deploy a simple Flask web application with Redis as a backend using **Kubernetes** running on **Minikube**.

It shows:
- Running a Python Flask app in containers
- Using Redis as a database
- Deploying to Kubernetes with Deployments, Services, and Pods
- Scaling Flask pods for load balancing

---

## 📦 Project Structure

```
k8s-flask-redis/
│
├── app/                  # Flask application source
│   ├── app.py            # Flask app entry point
│   ├── requirements.txt  # Python dependencies
│   └── Dockerfile        # Build image for Flask app
│
├── k8s/                  # Kubernetes manifests
│   ├── flask-deployment.yaml
│   ├── flask-service.yaml
│   ├── redis-deployment.yaml
│   ├── redis-service.yaml
│
└── README.md
```

---

## 🚀 Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)

Verify installation:

```bash
docker --version
minikube version
kubectl version --client
```

---

## ⚙️ Setup Instructions

### 1. Start Minikube
```bash
minikube start --driver=docker
```

### 2. Enable Minikube Docker Environment
```bash
eval $(minikube docker-env)   # Linux / macOS
# OR
minikube docker-env | Invoke-Expression   # PowerShell
```

### 3. Build the Flask Image inside Minikube
```bash
docker build -t flask-app ./app
```

### 4. Deploy to Kubernetes
```bash
kubectl apply -f k8s/
```

This will create:
- Flask Deployment (3 replicas by default)
- Flask Service (NodePort to expose externally)
- Redis Deployment (1 replica)
- Redis Service (ClusterIP)

---

## 🌐 Accessing the App

Get the Minikube IP:
```bash
minikube ip
```

Find the Flask Service NodePort:
```bash
kubectl get svc flask-service
```

Example output:
```
NAME            TYPE       CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
flask-service   NodePort   10.96.120.34   <none>        5000:30007/TCP   5m
```

Now open in browser:
```
http://<minikube-ip>:30007
```

---

## 📊 Scaling Flask Pods

Scale up to 5 replicas:
```bash
kubectl scale deployment flask-deployment --replicas=5
```

Check pods:
```bash
kubectl get pods
```

Kubernetes will load-balance requests between pods automatically via the Service.

---

## 🔧 Troubleshooting

- Check logs:
  ```bash
  kubectl logs <pod-name>
  ```
- Restart a pod:
  ```bash
  kubectl delete pod <pod-name>
  ```
- If Flask can’t connect to Redis, ensure `redis-service` is running:
  ```bash
  kubectl get svc
  ```

---

## 🛑 Stop the Cluster
```bash
minikube stop
```

---

## 📚 Learn More
- [Flask](https://flask.palletsprojects.com/)
- [Redis](https://redis.io/)
- [Kubernetes](https://kubernetes.io/)
- [Minikube](https://minikube.sigs.k8s.io/)
