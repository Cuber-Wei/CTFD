from datetime import datetime, timedelta
from CTFd.models import db, Challenges

def activate_blacklight_mode(start_time, end_time):
    """
    Activate blacklight mode within the specified time range.
    During this period, all challenge points will be set to 0.
    """
    current_time = datetime.now()
    
    if start_time <= current_time <= end_time:
        # Record current points of all challenges
        challenges = Challenges.query.all()
        original_points = {challenge.id: challenge.value for challenge in challenges}
        
        # Set all challenge points to 0
        for challenge in challenges:
            challenge.value = 0
        db.session.commit()
        
        return original_points
    else:
        return None

def restore_challenge_points(original_points):
    """
    Restore the original points of all challenges after blacklight mode ends.
    """
    if original_points:
        for challenge_id, points in original_points.items():
            challenge = Challenges.query.filter_by(id=challenge_id).first()
            if challenge:
                challenge.value = points
        db.session.commit()