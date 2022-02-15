from django.utils import timezone
from season.models import Season
from django.conf import settings
import smtplib
import email.message
from referee.models import Referee


def send_message(recipient, title, content):
    msg = email.message.Message()
    msg['Subject'] = f"[CCA] {title}"
    msg['From'] = settings.EMAIL_HOST_USER
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(content)
    s = smtplib.SMTP(host=settings.EMAIL_HOST, port=settings.EMAIL_PORT)
    s.starttls()
    s.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
    msg['To'] = recipient
    s.sendmail(msg['From'], [msg['To']], msg.as_string())
    s.quit()


def send_availability():
    with open("/tmp/refcalendar.log", "a") as f:
        f.write("Job : %s\r\n" % timezone.now())
    season = Season.objects.filter(active=True)[0]
    today = timezone.now().date()
    if season.start <= today <= season.end:
        f.write("in range\r\n")
        for ref in Referee.objects.filter(active=True):
            f.write(ref.user.email)
            # send_message(ref.user.email, season.title_email, season.content_email)
