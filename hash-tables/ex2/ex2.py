def reconstruct_trip(tickets):
     
  newTickets = dict((ticket) for ticket in tickets)
 
  location = None
  route = []
  def pieceTicket(loc):
     if(newTickets.get(loc)):
          route.append(newTickets.get(loc, "EndTicket"))
          print(route)
          location = newTickets.get(loc, "EndTicket")
          loca = newTickets.get(loc, "EndTicket")
          print(location, loca)
          if(location):
              pieceTicket(location)
  pieceTicket(location)
  if (len(route) < (len(newTickets) - 1)):
      return([])
  return(route)

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  reconstruct_trip([
          ('LHD', 'DAB'),
          (None, 'HVN'),
          ('MSO', 'SFO'),
          ('RDU', 'ABQ'),
          ('ACY', None),
  ])