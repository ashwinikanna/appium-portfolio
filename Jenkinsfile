pipeline {
  agent any
  options { timestamps() }

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Setup venv + install') {
      steps {
        sh '''
          set -e
          python3 -m venv .venv
          . .venv/bin/activate
         python -m pytest -q -m 'not mobile' || [ $? -eq 5 ]
        '''
      }
    }

    stage('Run tests') {
      steps {
        sh '''
          set -e
          . .venv/bin/activate
          python -m pytest -q
        '''
      }
    }
  }
}
