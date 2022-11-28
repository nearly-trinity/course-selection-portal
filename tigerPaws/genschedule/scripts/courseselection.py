from collections import defaultdict,deque
from genschedule.models import ClassData
from copy import deepcopy

def getOrder():
    """generates topological ordering of courses given prerequisites

    Returns:
        (List[String],dictionary[string,<ClassData obj>]): returns tuple of valid ordering and a lookup table for courses 
    """
    graph = defaultdict(list)
    course_dict = {} 
    indegree = {}

    # returns a query set of ClassData objects
    all_entries = ClassData.objects.all()
    all_courses = [entry.course for entry in all_entries]
    # some course (title) is dependent on prereqs (prereqs)
    for entry in all_entries:
        course = entry.course
        course_dict[course] = deepcopy(entry)
        prereqs = entry.prereqs.split(',')
        if prereqs == ['']:
            continue
        for c in prereqs:
            graph[c].append(course)

            # update or initalize the indegree of course
            indegree[course] = indegree.get(course,0)+1

    no_indegree_queue = deque([course for course in all_courses if course not in indegree])
    
    ordering = []
    while no_indegree_queue:
        course = no_indegree_queue.popleft()
        ordering.append(course)

        if course in graph:
            for neighbor in graph[course]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    no_indegree_queue.append(neighbor)

    return (ordering,course_dict)

# one from each here
applications_group = set(['CSCI-3311','CSCI-3342','CSCI-3343','CSCI-3344','CSCI-3353','CSCI-3354','CSCI-3366', 'CSCI-3195', 'CSCI-3295', 'CSCI-3395'])
systems_group = set(['CSCI-3323','CSCI-3334', 'CSCI-3196', 'CSCI-3296', 'CSCI-3396'])
design_group = set(['CSCI-3312', 'CSCI-3345', 'CSCI-3362', 'CSCI-3197', 'CSCI-3297', 'CSCI-3397'])

# all of the below
core_requirements = ['CSCI-1320','CSCI-1321','CSCI-1323','CSCI-2320','CSCI-2321','CSCI-2322','CSCI-3320','CSCI-3321','CSCI-3322']
senior_software = ['CSCI-4385','CSCI-4386']
thesis = ['CSCI-3398','CSCI-4399']

def generateSchedules(order, taken):
    """generates list of valid schedules

    Args:
        order (List[String]): topological ordering of classes
        taken (List[String]): courses that have already been taken by student

    Returns:
        List[List[List[String]]]: list of possible schedules divided by semester
    """
    # - need to take all core requirements and one course from each group
    # - pick either ss or thesis 
    # - take courses in groups of max 2


    path = []
    return path

def run():
    order,reference = getOrder()
    schedules = generateSchedules(order,[])




