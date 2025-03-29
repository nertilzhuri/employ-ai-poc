from match_crew.crew import MatchCrew

inputs = {
    'candidates_list': open('data/candidates.txt', 'r').read(),
    'jobs_list': open('data/jobs.txt', 'r').read(),
    'candidate': open('inputs/resume.txt', 'r').read(),
}

MatchCrew().crew().kickoff(inputs=inputs)