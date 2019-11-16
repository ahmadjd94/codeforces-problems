def cellCompete(states, days):
    if days ==0:
        return states
    else:
        result_states = []
        for r in range(len(states)):
            result_states.append(0)
            try:
                before_state = states[r-1]
            except:
                before_state = 0
            try:
                after_state = states[r+1]
            except:
                after_state = 0

            print((before_state==0 and after_state==0) or (before_state==1 and after_state==1))
            if (before_state==0 and after_state==0) or (before_state==1 and after_state==1):
                result_states[r]=0
            else:
                result_states[r]=1

            del(before_state)
            del(after_state)
        return cellCompete(result_states,days-1)

print cellCompete([0, 0, 1, 0, 1, 0, 0, 1],1)