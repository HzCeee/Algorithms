"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        employeeInfo = {}
        for employee in employees:
            employeeInfo[employee.id] = employee
            
        # return the importance of the given employee and all his subordinates
        def getImportanceHelper(employeeId):
            employee = employeeInfo[employeeId]
            importance = employee.importance
            if not employee.subordinates:
                return importance
            
            for subordinate in employee.subordinates:
                importance += getImportanceHelper(subordinate)
                
            return importance
        
        return getImportanceHelper(id)
        