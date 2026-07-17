class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        execution_stack, execution_times, last_timestamp = [], [0]*n, 0
        for log in logs:
            id, op, time = log.split(":")
            id, time = int(id), int(time)
            current = -1
            if op == 'start':
                execution_stack.append(id)
                current = execution_stack[-2] if len(execution_stack) > 1 else execution_stack[-1]
            else:
                time += 1
                current = execution_stack.pop()
            execution_times[current] += time - last_timestamp
            last_timestamp = time

        return execution_times

