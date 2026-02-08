pipeline {
  agent any

  options { timestamps() }

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Python check') {
      steps {
        sh '''
          set -e
          which python3
          python3 --version
        '''
      }
    }

    stage('Setup venv + install') {
  steps {
    sh '''
      set -e
      ls -la
      find . -maxdepth 2 -type f -name "requirements*.txt" -o -name "pyproject.toml" -o -name "Pipfile" -o -name "setup.py" | sed 's|^./||'
      python3 -m venv .venv
      . .venv/bin/activate
      python -m pip install --upgrade pip
    '''
  }
}


    stage('Run tests') {
      steps {
        sh '''
          set -e
          . .venv/bin/activate
          pytest -q
        '''
      }
    }
  }
}
