from collections import defaultdict,deque
from genschedule.models import ClassData

core_requirements = ['CSCI-1320','CSCI-1321','CSCI-1323','CSCI-2320','CSCI-2321','CSCI-2322','CSCI-3320','CSCI-3321','CSCI-3322']
applications_group = ['CSCI-3311','CSCI-3342','CSCI-3343','CSCI-3344','CSCI-3353','CSCI-3354','CSCI-3366', 'CSCI-3195', 'CSCI-3295', 'CSCI-3395']
systems_group = ['CSCI-3323','CSCI-3334', 'CSCI-3196', 'CSCI-3296', 'CSCI-3396']
design_group = ['CSCI-3312', 'CSCI-3345', 'CSCI-3362', 'CSCI-3197', 'CSCI-3297', 'CSCI-3397']

def queryDb():
    graph = defaultdict(list)
    indegree = {}

    # returns a query set of ClassData objects
    all_entries = ClassData.objects.all()
    all_courses = [entry.course for entry in all_entries]
    # some course (title) is dependent on prereqs (prereqs)
    for entry in all_entries:
        course = entry.course
        prereqs = entry.prereqs.split(',')
        if prereqs == ['']:
            continue
        for c in prereqs:
            graph[c].append(course)

            # update or initalize the indegree of course
            indegree[course] = indegree.get(course,0)+1
        
    # for start,ends in graph.items():
    # print(f"you need to take {start} to take: {ends}")
    # for course in all_courses:
    #     print(indegree[course])

    no_requirements_queue = deque([course for course in all_courses if course not in indegree])
    ordering = []

    while no_requirements_queue:
        course = no_requirements_queue.popleft()
        ordering.append(course)

        if course in graph:
            for neighbor in graph[course]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    no_requirements_queue.append(neighbor)

    return ordering

def order(graph):
    return

def buildGraph(dependencies):
    return


def run():
    queryDb()





