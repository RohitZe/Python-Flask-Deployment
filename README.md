# Python Flask CI/CD

A beginner-friendly project that demonstrates how a simple **Python Flask application moves from development to production** using Git, GitHub, Jenkins, and AWS.

> **Idea → Code → Git/GitHub → Automated Testing → Jenkins CI/CD → AWS Deployment → Users**

---

## 🧠 Project Intuition

Imagine we have an idea for a web application.

We first need to **turn that idea into code**. A developer writes the application using Python and Flask.

Once the code is written, we push it to **Git/GitHub** so that the source code is stored in a central place and other team members can access it.

The testing team can then pull the code, run it, and verify whether the application works correctly.

But there is a problem:

> What if developers push code every day and testers have to manually download, install dependencies, run tests, and check everything every time?

This is where **Jenkins** comes in.

Jenkins automates the repetitive steps involved in building and testing our application.

Finally, even if our application is successfully developed and tested, it is still running only in our development environment.

**Users around the world cannot access it yet.**

Therefore, we deploy the application to **AWS**, where it can run on production infrastructure and be accessed by users.

---

# 🔄 Overall CI/CD Flow

```text
                    IDEA
                     │
                     ▼
              Developer writes
                  Flask code
                     │
                     ▼
                Git Repository
                     │
                     ▼
                   GitHub
                     │
                     │  Code Push
                     ▼
                  Jenkins
                     │
             ┌───────┴────────┐
             ▼                ▼
          Build             Test
             │                │
             └───────┬────────┘
                     │
                  Success
                     │
                     ▼
                 Deploy
                     │
                     ▼
                    AWS
                     │
                     ▼
                  Internet
                     │
                     ▼
                   Users
```

---

# 🧩 What Does Each Part Do?

## 1. Python + Flask — Build the Application

First, we need to implement our idea.

For this project, we use **Python** as the programming language and **Flask** as the web framework.

Example:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, I am listening"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

### Intuition

Flask is responsible for running our web application.

It receives HTTP requests and returns responses.

```text
User
  │
  │ HTTP Request
  ▼
Flask
  │
  │ HTTP Response
  ▼
User
```

---

# 2. Git — Track Our Code

While developing, we don't want to lose previous versions of our code.

Git helps us track changes.

```text
Version 1
   ↓
Version 2
   ↓
Version 3
   ↓
Version 4
```

For example:

```bash
git add .
git commit -m "Add Flask application"
```

### Intuition

Think of Git as a **history book for your code**.

It allows us to know:

* What changed?
* Who changed it?
* When was it changed?
* What did the code look like previously?

---

# 3. GitHub — Store and Share the Code

After committing our code locally, we push it to GitHub.

```text
Developer Laptop
       │
       │ git push
       ▼
     GitHub
```

### Intuition

Git manages the code history locally.

GitHub provides a **central place where the repository can be stored and shared**.

Now other developers, testers, and automation tools can access the code.

---

# 4. Testing — Verify the Application

Before releasing our application, we need to make sure it works.

For example:

```python
def test_homepage():
    response = client.get("/")
    assert response.status_code == 200
```

### Intuition

Development answers:

> **"Did we build the feature?"**

Testing answers:

> **"Does the feature actually work?"**

Without testing, we could deploy broken code to production.

---

# 5. The Problem With Manual Testing

Imagine five developers are pushing code throughout the day.

Every time somebody pushes code, the testing team has to:

```text
Pull code
   ↓
Install dependencies
   ↓
Build application
   ↓
Run tests
   ↓
Check results
   ↓
Report result
```

Doing this manually is:

* Slow
* Repetitive
* Error-prone
* Difficult to scale

We want a machine to perform these repetitive steps.

---

# 6. Jenkins — Automation

This is where **Jenkins** comes into the picture.

Jenkins can automatically detect a change in our repository and execute a predefined pipeline.

```text
Developer
    │
    │ git push
    ▼
 GitHub
    │
    │ trigger
    ▼
 Jenkins
    │
    ├── Checkout code
    ├── Install dependencies
    ├── Build
    ├── Run tests
    └── Deploy
```

### Intuition

Think of Jenkins as an **automation worker**.

Instead of a person repeatedly saying:

> "Download the latest code, install everything, test it, and deploy it."

We tell Jenkins:

> **"Whenever new code arrives, perform these steps automatically."**

---

# 7. CI — Continuous Integration

CI stands for **Continuous Integration**.

The basic idea is:

> Developers frequently integrate their code into a shared repository, and automated systems verify that the new code works.

Example:

```text
Developer pushes code
        ↓
     GitHub
        ↓
     Jenkins
        ↓
   Run tests
        ↓
   Test passed ✅
```

If the test fails:

```text
Jenkins
   ↓
Test failed ❌
   ↓
Developer gets feedback
```

This allows problems to be discovered early.

---

# 8. CD — Continuous Delivery / Deployment

After the application passes the required checks, we can automate its release.

```text
Code
 ↓
Build
 ↓
Test
 ↓
Deploy
 ↓
AWS
```

This is the **CD** part of CI/CD.

Instead of manually logging into a server and copying application files, Jenkins can perform the deployment steps.

---

# 9. AWS — Production Environment

At this point, our application has been:

```text
Developed
   ↓
Tested
   ↓
Validated
```

But it is still running in our development environment.

For example:

```text
Developer Laptop
      │
      └── Flask application
```

The rest of the world cannot access our laptop as a reliable production server.

So we deploy the application to AWS.

```text
                    AWS
                     │
              ┌──────┴──────┐
              │              │
            Server        Network
              │
           Flask App
              │
              ▼
          Internet
              │
              ▼
            Users
```

Now users can access our application.

---

# 🌍 Development vs Production

### Development

```text
Developer Laptop
       │
       ▼
    Flask App
       │
       ▼
 localhost:5000
```

Only the development environment is running the application.

### Production

```text
                    AWS
                     │
                     ▼
                Flask App
                     │
                     ▼
                 Public IP
                     │
                     ▼
                 Internet
                     │
             ┌───────┴───────┐
             ▼               ▼
           User             User
```

Now the application is running on infrastructure designed to serve users.

---

# 🚀 Complete Project Journey

The entire project can be understood as one story:

### Step 1 — Idea

We have an idea for an application.

```text
💡 Idea
```

### Step 2 — Development

A developer converts the idea into code.

```text
💡 Idea
   ↓
Python + Flask
```

### Step 3 — Version Control

The developer tracks the code using Git.

```text
Code
 ↓
Git
```

### Step 4 — Collaboration

The code is pushed to GitHub.

```text
Developer
    ↓
   Git
    ↓
 GitHub
```

Now other developers and testers can access the source code.

### Step 5 — Automation

Jenkins automatically picks up the code.

```text
GitHub
   ↓
Jenkins
```

Jenkins can:

```text
Checkout
   ↓
Install dependencies
   ↓
Build
   ↓
Test
```

### Step 6 — Deployment

If everything succeeds:

```text
Jenkins
   ↓
Deploy
   ↓
AWS
```

### Step 7 — Users

Finally:

```text
AWS
 ↓
Internet
 ↓
Users 🌍
```

