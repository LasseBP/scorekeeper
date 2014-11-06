from scorekeeper import app

@app.route('/api/users/', methods=['GET', 'POST'])
def api_users():
    return 'users yo!'

@app.route('/api/users/<username>', methods=['GET', 'PUT', 'DELETE'])
def api_user(username):
    return 'user yo! ' + username

@app.route('/api/bets/', methods=['GET','POST'])
def api_bets():
    return 'bets yo!'

@app.route('/api/bets/<int:bet_id>', methods=['GET', 'PUT', 'DELETE'])
def api_bet(bet_id):
    return 'bets yo! ' + str(bet_id)

@app.route('/api/bets/<int:bet_id>/participants', methods=['GET', 'POST'])
def api_bet_participants(bet_id):
    return 'bets participants yo! ' + str(bet_id)

@app.route('/api/bets/<int:bet_id>/participants/<participant>', methods=['DELETE'])
def api_bet_delete_participant(bet_id, participant):
    return 'bets participants yo! ' + str(bet_id) + ' ' + participant

@app.route('/api/bets/<int:bet_id>/scorehistory', methods=['GET', 'POST'])
def api_bet_scorehistory(bet_id):
    return 'bets participants yo! ' + str(bet_id)

@app.route('/api/bets/<int:bet_id>/scorehistory/<int:change_id>', methods=['GET', 'POST'])
def api_bet_delete_scorehistory(bet_id, change_id):
    return 'bets participants yo! ' + str(bet_id) + ' ' + str(change_id)