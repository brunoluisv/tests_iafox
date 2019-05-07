pipeline {
  agent any
  stages {
    stage('Step #1'){
      steps{
        script{
          allure([
            includeProperties: false,
            jdk: '',
            properties: [],
            reportBuildPolicy: 'ALWAYS',
            results: [[path: 'allure-new']]
          ])
        }
        withPythonEnv('/usr/bin/python3'){
          sh 'pip3 install selenium'
          sh 'pip3 install pytest'
          sh 'pip3 install nose'
          sh 'pip3 install allure-pytest'
          sh 'chmod 777 geckodriver.log'
          sh 'py.test --alluredir=allure-new Test.py' 
        }
      }
    }
  }
}
