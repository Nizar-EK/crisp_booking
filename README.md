# Crisp Booking – Flask-baseret bookingsystem

Crisp Booking er et simpelt web-baseret bookingsystem udviklet i Python med Flask.  
Systemet gør det muligt for brugere at lave bordreservationer, og administratorer kan se og redigere alle bookings via et adminpanel.

Applikationen blev hostet på en **Azure Virtual Machine** med Gunicorn og Nginx som produktionssetup.

Projektet er lavet som en del af mit studie EK.

---

## Funktioner

- Opret og administrer bordreservationer  
- Adminpanel med overblik over alle bookings  
- Login-system til administrator  
- Validering af brugerinput  
- SQLite database til lagring af reservationer  
- Flask-template system (Jinja2) til visning af sider  
- Deployment på Azure VM (Gunicorn + Nginx)
- E-mailbekræftelser via Flask-mail
