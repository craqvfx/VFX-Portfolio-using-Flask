cd /d "D:\Coding Projects"
git clone https://github.com/craqvfx/VFX-Portfolio-using-Flask.git VFX-Portfolio-using-Flask
cd VFX-Portfolio-using-Flask
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
flask run