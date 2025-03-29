from resume_analyser_crew.crew import ResumeAnalyser



inputs = {
    'resume': open('inputs/resume.txt', 'r').read()
}

ResumeAnalyser().crew().kickoff(inputs=inputs)