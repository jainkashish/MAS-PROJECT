Calculate_si(chf_table, i):
begin
optimal = set()
payoff = 0
for curr_coalition in chf_table.key
  begin
   if agent i in curr_coalition and not in discard:
        begin
          curr_payoff = chf_table[key]/len(curr_coalition)
           if curr_payoff > payoff
            begin
              payoff = curr_payoff
               optimal = curr_coalition
            end
        end
    end
return payoff, optimal
end
