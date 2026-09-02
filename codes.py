#!/usr/bin/env python3
# Jenkins Pipeline Task Codes
# Based on the uploaded Pipeline Task and Addition Pipeline PDFs.
#
# The Jenkins Pipeline snippets are Groovy/Jenkinsfile code.
# The addition program is Python.

import sys
from pathlib import Path


# ============================================================
# ADDITION PROGRAM (add.py)
# ============================================================

def add_numbers(a, b):
    return a + b


def run_addition():
    if len(sys.argv) < 3:
        print("Usage: python jenkins_pipeline_codes.py <num1> <num2>")
        return

    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    result = add_numbers(num1, num2)

    print("=================================")
    print("Addition Result")
    print("=================================")
    print(f"First Number : {num1}")
    print(f"Second Number: {num2}")
    print(f"Sum         : {result}")


# ============================================================
# JENKINS PIPELINE TASK 1
# Checkout code and show files
# ============================================================

PIPELINE_TASK_1 = r"""
pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/your-username/your-repo.git'
            }
        }
        stage('Show Files') {
            steps {
                bat 'dir'
            }
        }
    }
}
"""


# ============================================================
# JENKINS PIPELINE TASK 2
# Checkout code and print current directory
# ============================================================

PIPELINE_TASK_2 = r"""
pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/your-username/your-repo.git'
            }
        }
        stage('Print Directory') {
            steps {
                bat 'cd'
            }
        }
    }
}
"""


# ============================================================
# JENKINS PIPELINE TASK 3
# Checkout code and print a message
# ============================================================

PIPELINE_TASK_3 = r"""
pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/your-username/your-repo.git'
            }
        }
        stage('Print Message') {
            steps {
                echo 'Hello! Jenkins Pipeline executed successfully'
            }
        }
    }
}
"""


# ============================================================
# JENKINS PIPELINE TASK 4
# Checkout code and create a file
# ============================================================

PIPELINE_TASK_4 = r"""
pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/your-username/your-repo.git'
            }
        }
        stage('Create File') {
            steps {
                bat 'echo This file is created by Jenkins > demo.txt'
            }
        }
    }
}
"""


# ============================================================
# JENKINS PIPELINE TASK 5
# Checkout code and read README.md
# ============================================================

PIPELINE_TASK_5 = r"""
pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/your-username/your-repo.git'
            }
        }
        stage('Read File') {
            steps {
                bat 'type README.md'
            }
        }
    }
}
"""


# ============================================================
# PARAMETERIZED ADDITION PIPELINE
# ============================================================

PARAMETERIZED_ADDITION_PIPELINE = r"""
pipeline {
    agent any

    parameters {
        string(
            name: 'BRANCH_NAME',
            defaultValue: 'main',
            description: 'Git branch'
        )
        string(
            name: 'NUM1',
            defaultValue: '10',
            description: 'First Number'
        )
        string(
            name: 'NUM2',
            defaultValue: '20',
            description: 'Second Number'
        )
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: "${params.BRANCH_NAME}",
                    url: 'https://github.com/Ramlingams/pipeline-parameters.git'
            }
        }

        stage('Addition Build') {
            steps {
                bat "python add.py ${params.NUM1} ${params.NUM2}"
            }
        }
    }
}
"""


# ============================================================
# HELPER: CREATE SEPARATE JENKINSFILES
# ============================================================

def save_jenkinsfiles(folder="jenkinsfiles"):
    path = Path(folder)
    path.mkdir(exist_ok=True)

    pipelines = {
        "Jenkinsfile_Task_1": PIPELINE_TASK_1,
        "Jenkinsfile_Task_2": PIPELINE_TASK_2,
        "Jenkinsfile_Task_3": PIPELINE_TASK_3,
        "Jenkinsfile_Task_4": PIPELINE_TASK_4,
        "Jenkinsfile_Task_5": PIPELINE_TASK_5,
        "Jenkinsfile_Addition": PARAMETERIZED_ADDITION_PIPELINE,
    }

    for filename, code in pipelines.items():
        (path / filename).write_text(code.strip() + "\n", encoding="utf-8")

    print(f"Created {len(pipelines)} Jenkinsfiles in: {path.resolve()}")


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        run_addition()
    else:
        save_jenkinsfiles()
