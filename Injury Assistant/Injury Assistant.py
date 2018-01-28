from tkinter import *
import webbrowser

root = Tk()
Intro = None
bill = None
Upper_Body = None
Lower_Body = None
arms = None
#global legs
legs = None
pelvis = None
torso = None
hips = None
tailbone = None
tendonsligaments = None
tendonsligamentsf = None
toes = None
ankles = None
muscles = None
feet = None
head = None
joints = None
jointsa = None
neck= None
hands = None
elbow = None
shoulder =None
wrist = None
back = None
chest = None
lungs = None
headache = None
mouth = None
ears = None
groin = None

"""

THIS STUFF IS UPPER BODY
   
"""

def UBC():
    global root, Upper_Body, Lower_body, Intro, bill, arms, torso, head
    Upper_Body.destroy()
    Intro.destroy()
    Lower_Body.destroy()
    bill = Label(root, text = "Where on your Upper Body does it hurt?", font=("fixedsys", 14), anchor=CENTER)
    
    armsi = PhotoImage(file="Minnehack\\arms.gif")
    arms = Button(root, image=armsi)
    arms.image = armsi
    arms.config(command = armsc)
    
    torsoi = PhotoImage(file="Minnehack\\torso.gif")
    torso = Button(root, image=torsoi)
    torso.image = torsoi
    torso.config(command = torsoc)
    
    headi = PhotoImage(file="Minnehack\\head.gif")
    head = Button(root, image=headi)
    head.image = headi
    head.config(command = headc)
    
    head.grid(row=2, column=2)
    torso.grid(row=2, column=1)
    arms.grid(row=2, column=0)
    bill.grid(row=1, column=0, columnspan=3)
    
    
def armsc():
    global root, bill, arms, legs, torso, head, musclesa, jointsa, tendonsligamentsa, hands
    arms.destroy()
    #legs.destroy()
    head.destroy()
    bill.destroy()
    torso.destroy()
    bill = Label(root, text = "Where on (or in) your Arms does it hurt?", font=("fixedsys", 14), anchor=CENTER)
    
    musclesai = PhotoImage(file="Minnehack\\muscles.gif")
    musclesa = Button(root, image=musclesai)
    musclesa.image = musclesai
    musclesa.config(command = musclesac)
    
    tendonsligamentsai = PhotoImage(file="Minnehack\\tendonsligaments.gif")
    tendonsligamentsa = Button(root, image=tendonsligamentsai)
    tendonsligamentsa.image = tendonsligamentsai
    tendonsligamentsa.config(command = tendonsligamentsac)
    
    jointsai = PhotoImage(file="Minnehack\\jointsa.gif")
    jointsa = Button(root, image=jointsai)
    jointsa.image = jointsai
    jointsa.config(command = jointsac)
    
    handsi = PhotoImage(file="Minnehack\\hands.gif")
    hands = Button(root, image=handsi)
    hands.image = handsi
    hands.config(command = handsc)
    
    hands.grid(row=2, column=1)
    musclesa.grid(row=2, column=0)
    tendonsligamentsa.grid(row=1, column=1)
    jointsa.grid(row=1, column=0)
    bill.grid(row=0, column=0, columnspan=2)
    
def musclesac():
    global root, Upper_Body, Lower_body, Intro, bill, arms, torso, head, musclesa, tendonsligamentsa, jointsa, hands
    musclesa.destroy()
    jointsa.destroy()
    hands.destroy()
    bill.destroy()
    tendonsligamentsa.destroy()
    bill = Label(root, text = "Common issues with arm muscles", font=("fixedsys", 14), anchor=CENTER)
    
    Info = Label(root, text= "The biceps muscle is located at the front of your upper arm. \nThe muscle has two tendons that attach it to the bones of the \nshoulder and one tendon that attaches to the radius bone at the elbow.\n \nThe tricep is located at the back of the upper arm, and may also sustain \ninjuries worthy of a visit to the hospital.\n \n If you suspect you have a sprained muscle, a common household remedy\n is an ice pack. Other options to relieve pain are available.\n If you suspect a muscle has been torn, it is advisable that you go\n to the hospital and seek treatment. Signs of a torn muscle include:\n Inability to use the affected muscle\n Intense pain in the affected area\n May feel similar to a broken bone in some circumstances.\n\nIf you feel that you may have a strained or sprained muscle, you may click the buttons below to view web pages on this subject.", font=("fixedsys", 14), anchor=CENTER)
    
    #mayoi = PhotoImage(file="Minnehack\\mayo.gif")
    mayo = Button(root, text='Mayo Clinic')
    #mayo.image = mayoi
    new=1
    urlm = "https://www.mayoclinic.org/symptoms/muscle-pain/basics/definition/sym-20050866"
    def openmayo():
        webbrowser.open(urlm, new=new)
    mayo.config(command = openmayo)
    
    #clevelandi = PhotoImage(file="Minnehack\\mayo.gif")
    cleveland = Button(root, text='Cleveland Clinic')
    #cleveland.image = clevelandi
    new=1
    urlc = "https://my.clevelandclinic.org/health/articles/14534-biceps-tendon-injuries"
    def opencleveland():
        webbrowser.open(urlc, new=new)
    cleveland.config(command = opencleveland)
    
    cleveland.grid(row=1, column=1)
    mayo.grid(row=1, column=0)
    Info.grid(row=0, column=0, columnspan=2)
    
def handsc():
    global root, Upper_Body, Lower_body, Intro, bill, arms, torso, head, musclesa, tendonsligamentsa, jointsa, hands
    musclesa.destroy()
    jointsa.destroy()
    hands.destroy()
    bill.destroy()
    tendonsligamentsa.destroy()
    bill = Label(root, text = "Common issues with hands.", font=("fixedsys", 14), anchor=CENTER)
    
    Info = Label(root, text = "The hand is an oft used tool, and as such tends to sustain many injuries.\n Sprains and strains are the most likely cuprit of your pain, but if you can't\n move your hand, it could be broken. Torn or excessively stretched\n muscles may require medical attention. Milder sprains may be treatable with an ice pack.\n If you suspect you may have a worse affliction, please visit a doctor or view these websites to get more information.", font=("fixedsys", 14), anchor=CENTER)
    
        #mayoi = PhotoImage(file="Minnehack\\mayo.gif")
    mayo = Button(root, text='MyHealth Alberta')
    #mayo.image = mayoi
    new=1
    urlm = "https://myhealth.alberta.ca/Health/aftercareinformation/pages/conditions.aspx?hwid=uf7014"
    def openmayo():
        webbrowser.open(urlm, new=new)
    mayo.config(command = openmayo)
    
    #clevelandi = PhotoImage(file="Minnehack\\mayo.gif")
    cleveland = Button(root, text='National Institutes of Health')
    #cleveland.image = clevelandi
    new=1
    urlc = "https://www.niams.nih.gov/health-topics/sprains-and-strains"
    def opencleveland():
        webbrowser.open(urlc, new=new)
    cleveland.config(command = opencleveland)
    
    cleveland.grid(row=2, column=1)
    mayo.grid(row=2, column=0)
    Info.grid(row=1, column=0, columnspan=2)
    bill.grid(row=0, column=0, columnspan=2)
    
def tendonsligamentsac():
    global root, Upper_Body, Lower_body, Intro, bill, arms, torso, head, musclesa, tendonsligamentsa, jointsa, hands
    musclesa.destroy()
    jointsa.destroy()
    hands.destroy()
    bill.destroy()
    tendonsligamentsa.destroy()
    bill = Label(root, text = "Issues with tendons (in arms)", font=("fixedsys", 14), anchor=CENTER)
    
    Info = Label(root, text = "Tendonitis is the inflammation of tendons, leading to pain and \n possibly reduced range of motion depending on the pain level.\n Torn tendons can cause a loss of movement, as they are what\n connect the muscles to the bones. If you are fortunate enough to\n only have tendonitis, it can potentially be treated with ice and rest.\n A torn tendon often requires medical attention to properly heal. Below \n are two websites which contain more information on the subject. \n\nIf you suspect you have a torn or stretched tendon, your doctor may have a plan to speed up recovery.", font=("fixedsys", 14), anchor=CENTER)
    
        #mayoi = PhotoImage(file="Minnehack\\mayo.gif")
    mayo = Button(root, text='Cleveland Clinic')
    #mayo.image = mayoi
    new=1
    urlm = "https://my.clevelandclinic.org/health/articles/14534-biceps-tendon-injuries"
    def openmayo():
        webbrowser.open(urlm, new=new)
    mayo.config(command = openmayo)
    
    #clevelandi = PhotoImage(file="Minnehack\\mayo.gif")
    cleveland = Button(root, text='Mayo Clinic')
    #cleveland.image = clevelandi
    new=1
    urlc = "https://www.mayoclinic.org/diseases-conditions/sprains-and-strains/symptoms-causes/syc-20377938"
    def opencleveland():
        webbrowser.open(urlc, new=new)
    cleveland.config(command = opencleveland)
    
    cleveland.grid(row=2, column=1)
    mayo.grid(row=2, column=0)
    Info.grid(row=1, column=0, columnspan=2)
    bill.grid(row=0, column=0, columnspan=2)
    
def jointsac():
    global root, Upper_Body, Lower_body, Intro, bill, arms, torso, head, musclesa, tendonsligamentsa, jointsa, hands, shoulder, wrist, elbow
    jointsa.destroy()
    tendonsligamentsa.destroy()
    musclesa.destroy()
    bill.destroy()
    hands.destroy()
    bill = Label(root, text = "Which joint is the problem?", font=("fixedsys", 14), anchor=CENTER)
    
    elbowi = PhotoImage(file="Minnehack\\elbow.gif")
    elbow = Button(root, image=elbowi)
    elbow.image = elbowi
    elbow.config(command = elbowc)
    
    wristi = PhotoImage(file="Minnehack\\wrist.gif")
    wrist = Button(root, image=wristi)
    wrist.image = wristi
    wrist.config(command = wristc)
    
    shoulderi = PhotoImage(file="Minnehack\\shoulder.gif")
    shoulder = Button(root, image=shoulderi)
    shoulder.image = shoulderi
    shoulder.config(command = shoulderc)
    
    elbow.grid(row=1, column=2)
    wrist.grid(row=1, column=1)
    shoulder.grid(row=1, column=0)
    bill.grid(row=0, column=0, columnspan=3)

def elbowc():
    global root, Upper_Body, Lower_body, Intro, bill, arms, torso, head, musclesa, tendonsligamentsa, jointsa, hands, elbow, shoulder, wrist
    bill.destroy()
    wrist.destroy()
    shoulder.destroy()
    elbow.destroy()
    bill = Label(text = 'So the elbow\'s the issue, eh?', font=("fixedsys", 14), anchor=CENTER)
    Info = Label(root, text = "Bursitis (bur-SY-tis) is a painful condition that affects the small, \nfluid-filled sacs — called bursae (bur-SEE) — that cushion the bones, tendons\n and muscles near your joints. Bursitis occurs when bursae become inflamed. \nSymptoms include; Feeling achy or stiff, Hurting more when you \nmove it or press on it, Looking swollen and red. Elbows may also become \ndislocated, an extremely painful afflictment. This is often obvious to \nthe person suffering this. If this happens often, see \na physician. Tendons attatched to the elbow may also snap or break, \nbut more info on that may be found in the Tendons and Ligaments section. \n\nTwo links are provided below where more info may be obtained.", font=("fixedsys", 14), anchor=CENTER)
    
        #mayoi = PhotoImage(file="Minnehack\\mayo.gif")
    mayo = Button(root, text='Mayo Clinic')
    #mayo.image = mayoi
    new=1
    urlm = "https://www.mayoclinic.org/diseases-conditions/dislocated-elbow/symptoms-causes/syc-20371688"
    def openmayo():
        webbrowser.open(urlm, new=new)
    mayo.config(command = openmayo)
    
    #clevelandi = PhotoImage(file="Minnehack\\mayo.gif")
    cleveland = Button(root, text='OrthoInfo (AAOS)')
    #cleveland.image = clevelandi
    new=1
    urlc = "https://orthoinfo.aaos.org/en/diseases--conditions/elbow-olecranon-bursitis/"
    def opencleveland():
        webbrowser.open(urlc, new=new)
    cleveland.config(command = opencleveland)
    
    cleveland.grid(row=2, column=1)
    mayo.grid(row=2, column=0)
    Info.grid(row=1, column=0, columnspan=2)
    bill.grid(row=0, column=0, columnspan=3)
    
def shoulderc():
    global root, Upper_Body, Lower_body, Intro, bill, arms, torso, head, musclesa, tendonsligamentsa, jointsa, hands, elbow, shoulder, wrist
    bill.destroy()
    wrist.destroy()
    shoulder.destroy()
    elbow.destroy()
    bill = Label(text = 'So the shoulder\'s the issue, eh?', font=("fixedsys", 14), anchor=CENTER)
    Info = Label(root, text = "A separated shoulder is an injury to the ligaments that hold your collarbone (clavicle) to your shoulder blade. \nIn a mild separated shoulder, the ligaments might just be stretched. In severe injuries, ligaments might be torn.\n Shoulders may also be dislocated, and tendons/ligaments attatched to the shoulder may break.\n\nTwo links are provided below where more info may be obtained.", font=("fixedsys", 14), anchor=CENTER)
    
        #mayoi = PhotoImage(file="Minnehack\\mayo.gif")
    mayo = Button(root, text='National Institutes of Health')
    #mayo.image = mayoi
    new=1
    urlm = "https://www.niams.nih.gov/health-topics/shoulder-problems"
    def openmayo():
        webbrowser.open(urlm, new=new)
    mayo.config(command = openmayo)
    
    #clevelandi = PhotoImage(file="Minnehack\\mayo.gif")
    cleveland = Button(root, text='OrthoInfo (AAOS)')
    #cleveland.image = clevelandi
    new=1
    urlc = "https://orthoinfo.aaos.org/en/diseases--conditions/shoulder-pain-and-common-shoulder-problems/"
    def opencleveland():
        webbrowser.open(urlc, new=new)
    cleveland.config(command = opencleveland)
    
    cleveland.grid(row=2, column=1)
    mayo.grid(row=2, column=0)
    Info.grid(row=1, column=0, columnspan=2)
    bill.grid(row=0, column=0, columnspan=3)
    
def wristc():
    global root, Upper_Body, Lower_body, Intro, bill, arms, torso, head, musclesa, tendonsligamentsa, jointsa, hands, elbow, shoulder, wrist
    bill.destroy()
    wrist.destroy()
    shoulder.destroy()
    elbow.destroy()
    bill = Label(text = 'So the wrist\'s the issue, eh?', font=("fixedsys", 14), anchor=CENTER)
    Info = Label(root, text = "Colles' fractures are very common; they're the most frequently broken \nbone in the arm. In the United States, one out of every 10 broken bones is a broken wrist.\n Carpal tunnel is a common ailment among people in professions requiring extended\n keyboard use. Braces and pads can be bought to alleviate pain.\n Sprained or strained wrists are not uncommon either.\nIf you suspect something more serious has happened to your \nwrist, an x-ray may be necessary to determine he cause of your pain.\n\nTwo links are provided below where more info may be obtained.", font=("fixedsys", 14), anchor=CENTER)
    
        #mayoi = PhotoImage(file="Minnehack\\mayo.gif")
    mayo = Button(root, text='OrthoInfo (AAOS)')
    #mayo.image = mayoi
    new=1
    urlm = "https://orthoinfo.aaos.org/en/diseases--conditions/carpal-tunnel-syndrome/"
    def openmayo():
        webbrowser.open(urlm, new=new)
    mayo.config(command = openmayo)
    
    #clevelandi = PhotoImage(file="Minnehack\\mayo.gif")
    cleveland = Button(root, text='Mayo Clinic')
    #cleveland.image = clevelandi
    new=1
    urlc = "https://www.mayoclinic.org/diseases-conditions/broken-wrist-broken-hand/symptoms-causes/syc-20353169"
    def opencleveland():
        webbrowser.open(urlc, new=new)
    cleveland.config(command = opencleveland)
    
    cleveland.grid(row=2, column=1)
    mayo.grid(row=2, column=0)
    Info.grid(row=1, column=0, columnspan=2)
    bill.grid(row=0, column=0, columnspan=3)
    
def torsoc():
    global root, bill, arms, legs, pelvis, torso, head, lungs, back, chest
    arms.destroy()
    head.destroy()
    #legs.destroy()
    bill.destroy()
    #pelvis.destroy()
    torso.destroy()
    bill = Label(root, text = "Where on (or in) your Torso does it hurt?", font=("fixedsys", 14), anchor=CENTER)
    
    lungsi = PhotoImage(file="Minnehack\\lungs.gif")
    lungs = Button(root, image=lungsi)
    lungs.image = lungsi
    lungs.config(command = lungsc)
    
    chesti = PhotoImage(file="Minnehack\\chest.gif")
    chest = Button(root, image =chesti)
    chest.image = chesti
    chest.config(command = chestc)
    
    backi = PhotoImage(file="Minnehack\\back.gif")
    back = Button(root, image=backi)
    back.image = backi
    back.config(command = backc)
    
    lungs.grid(row=1, column=2)
    chest.grid(row=1, column=1)
    back.grid(row=1, column=0)
    bill.grid(row=0, column=0, columnspan=3)
    
def headc():
    global root, bill, arms, legs, pelvis, torso, head, neck, headache, ears, mouth
    arms.destroy()
    head.destroy()
    #legs.destroy()
    bill.destroy()
    #pelvis.destroy()
    torso.destroy()
    bill = Label(root, text = "What seems to be the problem?", font=("fixedsys", 14), anchor=CENTER)
    
    headachei = PhotoImage(file="Minnehack\\headache.gif")
    headache = Button(root, image=headachei)
    headache.image = headachei
    headache.config(command = headachec)
    
    earsi = PhotoImage(file="Minnehack\\ears.gif")
    ears = Button(root, image=earsi)
    ears.image = earsi
    ears.config(command = earsc)
    
    mouthi = PhotoImage(file="Minnehack\\mouth.gif")
    mouth = Button(root, image=mouthi)
    mouth.image = mouthi
    mouth.config(command = mouthc)
    
    necki = PhotoImage(file="Minnehack\\neck.gif")
    neck = Button(root, image=necki)
    neck.image = necki
    neck.config(command = neckc)
    
    neck.grid(row=2, column=1)
    mouth.grid(row=2, column=0)
    ears.grid(row=1, column=1)
    headache.grid(row=1, column=0)
    bill.grid(row=0, column=0, columnspan=3)
    
def lungsc():
    global root, Upper_Body, Lower_body, Intro, bill, arms, torso, head, musclesa, tendonsligamentsa, jointsa, hands, elbow, shoulder, wrist, back, chest, lungs
    back.destroy()
    chest.destroy()
    lungs.destroy()
    #elbow.destroy()
    bill.destroy()
    bill = Label(text = 'So the lungs are the issue, eh?', font=("fixedsys", 14), anchor=CENTER)
    Info = Label(root, text = "Lung pain can be caused my multiple things, so it is important\n to be careful in determining the risk of letting pain go unchecked.\n A punctured lung, for instance, is a serious threat, and requires surgery to properly fix.\n Other issues, such as asthma, may make it difficult to catch your breath after strenuous activities.\n Talk with your doctor if you think you have either of these problems, \n and you may also visit these websites if you wish to read up on lung injuries.", font=("fixedsys", 14), anchor=CENTER)
    
        #mayoi = PhotoImage(file="Minnehack\\mayo.gif")
    mayo = Button(root, text='US National Library of Medicine')
    #mayo.image = mayoi
    new=1
    urlm = "https://medlineplus.gov/ency/article/000087.htm"
    def openmayo():
        webbrowser.open(urlm, new=new)
    mayo.config(command = openmayo)
    
    #clevelandi = PhotoImage(file="Minnehack\\mayo.gif")
    cleveland = Button(root, text='Mayo Clinic')
    #cleveland.image = clevelandi
    new=1
    urlc = "https://www.mayoclinic.org/diseases-conditions/asthma/symptoms-causes/syc-20369653"
    def opencleveland():
        webbrowser.open(urlc, new=new)
    cleveland.config(command = opencleveland)
    
    cleveland.grid(row=2, column=1)
    mayo.grid(row=2, column=0)
    Info.grid(row=1, column=0, columnspan=2)
    bill.grid(row=0, column=0, columnspan=3)
    
def backc():
    global root, Upper_Body, Lower_body, Intro, bill, arms, torso, head, musclesa, tendonsligamentsa, jointsa, hands, elbow, shoulder, wrist, back, chest, lungs
    back.destroy()
    chest.destroy()
    lungs.destroy()
    #elbow.destroy()
    bill.destroy()
    bill = Label(text = 'So your back is the issue, eh?', font=("fixedsys", 14), anchor=CENTER)
    Info = Label(root, text = "Back problems are tough to ignore and can pose a serious threat to your health.\n The discs in your spine are especially notiecable when something goes wrong.\n A slipped or herniated disc is a painful experience, and you will want to fix it right away if possible.\n Suffering a twisted back is also painful, and it is reccomended that you\n visit a doctor to get the help you need.\n\n The websites below have info on various back issues, should you choose to browse.", font=("fixedsys", 14), anchor=CENTER)
    
        #mayoi = PhotoImage(file="Minnehack\\mayo.gif")
    mayo = Button(root, text='Mayo Clinic')
    #mayo.image = mayoi
    new=1
    urlm = "https://www.mayoclinic.org/diseases-conditions/herniated-disk/symptoms-causes/syc-20354095"
    def openmayo():
        webbrowser.open(urlm, new=new)
    mayo.config(command = openmayo)
    
    #clevelandi = PhotoImage(file="Minnehack\\mayo.gif")
    cleveland = Button(root, text='Natnl. Inst. of Neurological Disorders and Stroke')
    #cleveland.image = clevelandi
    new=1
    urlc = "https://www.ninds.nih.gov/Disorders/Patient-Caregiver-Education/Fact-Sheets/Low-Back-Pain-Fact-Sheet"
    def opencleveland():
        webbrowser.open(urlc, new=new)
    cleveland.config(command = opencleveland)
    
    cleveland.grid(row=2, column=1)
    mayo.grid(row=2, column=0)
    Info.grid(row=1, column=0, columnspan=2)
    bill.grid(row=0, column=0, columnspan=3)
    
def chestc():
    global root, Upper_Body, Lower_body, Intro, bill, arms, torso, head, musclesa, tendonsligamentsa, jointsa, hands, elbow, shoulder, wrist, back, chest, lungs
    back.destroy()
    chest.destroy()
    lungs.destroy()
    #elbow.destroy()
    bill.destroy()
    bill = Label(text = 'So your chest is the issue, eh?', font=("fixedsys", 14), anchor=CENTER)
    Info = Label(root, text = "If you have extreme chest pain, visit a doctor or call an ambulance immediately.\n This pain could be indicative of a Heart Attack or Stroke, both of which are deadly phenomenon. \nOther chest pains may be very benign, such as heartburn, \nso it is important to pinpoint where the pain is coming from. \n\nHere are two links which may help to determine the cause of your chest pains.", font=("fixedsys", 14), anchor=CENTER)
    
        #mayoi = PhotoImage(file="Minnehack\\mayo.gif")
    mayo = Button(root, text='Mayo Clinic')
    #mayo.image = mayoi
    new=1
    urlm = "https://www.mayoclinic.org/diseases-conditions/chest-pain/symptoms-causes/syc-20370838"
    def openmayo():
        webbrowser.open(urlm, new=new)
    mayo.config(command = openmayo)
    
    #clevelandi = PhotoImage(file="Minnehack\\mayo.gif")
    cleveland = Button(root, text='Cleveland Clinic')
    #cleveland.image = clevelandi
    new=1
    urlc = "https://health.clevelandclinic.org/2015/03/3-types-of-chest-pain-that-wont-kill-you/"
    def opencleveland():
        webbrowser.open(urlc, new=new)
    cleveland.config(command = opencleveland)
    
    cleveland.grid(row=2, column=1)
    mayo.grid(row=2, column=0)
    Info.grid(row=1, column=0, columnspan=2)
    bill.grid(row=0, column=0, columnspan=3)
    
def neckc():
    global root, Upper_Body, Lower_body, Intro, bill, arms, torso, head, musclesa, tendonsligamentsa, jointsa, hands, elbow, shoulder, wrist, back, chest, lungs, ears, headache, mouth, neck
    headache.destroy()
    mouth.destroy()
    neck.destroy()
    ears.destroy()
    bill.destroy()
    bill = Label(text = 'Neck pains got ya?', font=("fixedsys", 14), anchor=CENTER)
    
    Info = Label(root, text = "A sprained neck is painful, and often a distracting experience.\n If the issue is fairly tough to deal with, \nit is advisable to put on some ice and relax the muscles. \nSome neck injuries can be more serious than others, and may require a neck brace to recover from.\n\nBelow are two links to places where you can learn about the specifics on neck injuries.", font=("fixedsys", 14), anchor=CENTER)
    
        #mayoi = PhotoImage(file="Minnehack\\mayo.gif")
    mayo = Button(root, text='Mayo Clinic')
    #mayo.image = mayoi
    new=1
    urlm = "https://www.mayoclinic.org/diseases-conditions/neck-pain/symptoms-causes/syc-20375581"
    def openmayo():
        webbrowser.open(urlm, new=new)
    mayo.config(command = openmayo)
    
    #clevelandi = PhotoImage(file="Minnehack\\mayo.gif")
    cleveland = Button(root, text='British NHS')
    #cleveland.image = clevelandi
    new=1
    urlc = "https://www.nhs.uk/conditions/neck-pain-and-stiff-neck/"
    def opencleveland():
        webbrowser.open(urlc, new=new)
    cleveland.config(command = opencleveland)
    
    cleveland.grid(row=2, column=1)
    mayo.grid(row=2, column=0)
    Info.grid(row=1, column=0, columnspan=2)
    bill.grid(row=0, column=0, columnspan=3)
    
    
def headachec():
    global root, Upper_Body, Lower_body, Intro, bill, arms, torso, head, musclesa, tendonsligamentsa, jointsa, hands, elbow, shoulder, wrist, back, chest, lungs, ears, headache, mouth, neck
    headache.destroy()
    mouth.destroy()
    neck.destroy()
    ears.destroy()
    bill.destroy()
    bill = Label(text = 'Headaches are a pain in the (area above the) neck.', font=("fixedsys", 14), anchor=CENTER)
    
    Info = Label(root, text = "Intense or mild head pain following a collision or head injury may indicate a concussion has occured.\n These are potentially life threatening and have specific setps that should be taken to minimize damage.\nHeadaches affect nearly everyone, but to different degrees.\n Migranes are headaches that last for long periods of time, at high pain levels.\n Without treatment, they can have a large negative impact on ones life. \n Other people experience less frequent, low intensity headaches.\n These can be caused by things such as staring at electronic screens for too long, \n or from being dehydrated. Many people experience headaches at different intensities, \n so your experience may not be the same as someone elses.\n\n Below are two links which detail some causes and treatments for headaches.", font=("fixedsys", 14), anchor=CENTER)
    
        #mayoi = PhotoImage(file="Minnehack\\mayo.gif")
    mayo = Button(root, text='Mayo Clinic')
    #mayo.image = mayoi
    new=1
    urlm = "https://www.mayoclinic.org/diseases-conditions/migraine-headache/symptoms-causes/syc-20360201"
    def openmayo():
        webbrowser.open(urlm, new=new)
    mayo.config(command = openmayo)
    
    #clevelandi = PhotoImage(file="Minnehack\\mayo.gif")
    cleveland = Button(root, text='Cleaveland Clinic')
    #cleveland.image = clevelandi
    new=1
    urlc = "https://my.clevelandclinic.org/health/articles/8262-headache-treatment-overview"
    def opencleveland():
        webbrowser.open(urlc, new=new)
    cleveland.config(command = opencleveland)
    
    cleveland.grid(row=2, column=1)
    mayo.grid(row=2, column=0)
    Info.grid(row=1, column=0, columnspan=2)
    bill.grid(row=0, column=0, columnspan=3)
    
def mouthc():
    global root, Upper_Body, Lower_body, Intro, bill, arms, torso, head, musclesa, tendonsligamentsa, jointsa, hands, elbow, shoulder, wrist, back, chest, lungs, ears, headache, mouth, neck
    headache.destroy()
    mouth.destroy()
    neck.destroy()
    ears.destroy()
    bill.destroy()
    bill = Label(text = 'Mouth Pains and what might cause them.', font=("fixedsys", 14), anchor=CENTER)
    
    Info = Label(root, text = "Pains in the mouth or teeth are sometimes the result of dental hygene issues.\n If a tooth hurts, it may need to be removed to protect you from bacteria entering your jaw.\n A painful cheek or gum spot may indicate a sore that has developed due to irritation.\n \nBelow are two websites that have information on what may cause a few forms of dental pain.", font=("fixedsys", 14), anchor=CENTER)
    
        #mayoi = PhotoImage(file="Minnehack\\mayo.gif")
    mayo = Button(root, text='British NHS')
    #mayo.image = mayoi
    new=1
    urlm = "https://www.nhs.uk/conditions/Toothache/"
    def openmayo():
        webbrowser.open(urlm, new=new)
    mayo.config(command = openmayo)
    
    #clevelandi = PhotoImage(file="Minnehack\\mayo.gif")
    cleveland = Button(root, text='Mayo Clinic')
    #cleveland.image = clevelandi
    new=1
    urlc = "https://www.mayoclinic.org/diseases-conditions/canker-sore/symptoms-causes/syc-20370615"
    def opencleveland():
        webbrowser.open(urlc, new=new)
    cleveland.config(command = opencleveland)
    
    cleveland.grid(row=2, column=1)
    mayo.grid(row=2, column=0)
    Info.grid(row=1, column=0, columnspan=2)
    bill.grid(row=0, column=0, columnspan=3)
    
def earsc():
    global root, Upper_Body, Lower_body, Intro, bill, arms, torso, head, musclesa, tendonsligamentsa, jointsa, hands, elbow, shoulder, wrist, back, chest, lungs, ears, headache, mouth, neck
    headache.destroy()
    mouth.destroy()
    neck.destroy()
    ears.destroy()
    bill.destroy()
    bill = Label(text = 'Earaches and balance issues.', font=("fixedsys", 14), anchor=CENTER)
    
    Info = Label(root, text = "Ear infections can cause pain and swelling in the inner ears,\n causing difficulty in balancing, as your body is unable to get the signals it needs \n from the fluid filled areas in your inner ear. \n Earaches can be caused by damage to the eardrum, which may produce a ringing noice in some cases.\n While not all earaches are dangerous, they are certainly unpleasent\n and may be treatable should you seek treatment.\n\n Below are two links which you may follow to find more info on these subjects.", font=("fixedsys", 14), anchor=CENTER)
    
        #mayoi = PhotoImage(file="Minnehack\\mayo.gif")
    mayo = Button(root, text='British NHS')
    #mayo.image = mayoi
    new=1
    urlm = "https://www.nhs.uk/conditions/earache/"
    def openmayo():
        webbrowser.open(urlm, new=new)
    mayo.config(command = openmayo)
    
    #clevelandi = PhotoImage(file="Minnehack\\mayo.gif")
    cleveland = Button(root, text='Cleveland Clinic')
    #cleveland.image = clevelandi
    new=1
    urlc = "https://my.clevelandclinic.org/health/diseases/16944-ear-infections"
    def opencleveland():
        webbrowser.open(urlc, new=new)
    cleveland.config(command = opencleveland)
    
    cleveland.grid(row=2, column=1)
    mayo.grid(row=2, column=0)
    Info.grid(row=1, column=0, columnspan=2)
    bill.grid(row=0, column=0, columnspan=3)
    
"""

THIS STUFF IS LOWER BODY
   
"""
   
def LBC():
    global root, Upper_Body, Lower_body, Intro, bill, legs, pelvis
    Upper_Body.destroy()
    Intro.destroy()
    Lower_Body.destroy()
    bill = Label(root, text = "Where on your Lower Body does it hurt?", font=("fixedsys", 14), anchor=CENTER)
    
    legsi = PhotoImage(file="Minnehack\\legs.gif")
    legs = Button(root, image=legsi)
    legs.image = legsi
    legs.config(command = legsc)
    
    pelvisi = PhotoImage(file="Minnehack\\pelvis.gif")
    pelvis = Button(root, image=pelvisi)
    pelvis.image = pelvisi
    pelvis.config(command = pelvisc)
    
    pelvis.grid(row=2, column=1)
    legs.grid(row=2, column=0)
    bill.grid(row=1, column=0, columnspan=2)
    
def legsc():
    global root, Upper_Body, Lower_body, Intro, bill, arms, legs, pelvis, tendonsligaments, muscles, feet, joints
    #arms.destroy()
    legs.destroy()
    bill.destroy()
    pelvis.destroy()
    bill = Label(root, text = "Where on (or in) your Legs does it hurt?", font=("fixedsys", 14), anchor=CENTER)
    
    musclesi = PhotoImage(file="Minnehack\\muscles.gif")
    muscles = Button(root, image=musclesi)
    muscles.image = musclesi
    muscles.config(command = musclesc)
    
    tendonsligamentsi = PhotoImage(file="Minnehack\\tendonsligaments.gif")
    tendonsligaments = Button(root, image=tendonsligamentsi)
    tendonsligaments.image = tendonsligamentsi
    tendonsligaments.config(command = tendonsligamentsc)
    
    feeti = PhotoImage(file="Minnehack\\feet.gif")
    feet = Button(root, image=feeti)
    feet.image = feeti
    feet.config(command = feetc)
    
    jointsi = PhotoImage(file="Minnehack\\joints.gif")
    joints = Button(root, image=jointsi)
    joints.image = jointsi
    joints.config(command = jointsc)
    
    joints.grid(row=2, column=1)
    feet.grid(row=2, column=0)
    tendonsligaments.grid(row=1, column=0)
    muscles.grid(row=1, column=1)
    bill.grid(row=0, column=0, columnspan=3)
    
def musclesc():
    #end of line
    global root, Upper_Body, Lower_body, Intro, bill, arms, legs, pelvis, tendonsligaments, muscles, feet, joints
    pelvis.destroy()
    legs.destroy()
    bill.destroy()
    joints.destroy()
    feet.destroy()
    tendonsligaments.destroy()
    muscles.destroy()
    
    bill = Label(text = 'Sore or painful leg muscles.', font=("fixedsys", 14), anchor=CENTER)
    
    Info = Label(root, text = "Much like with arms, leg muscles can be torn or sprained,\n and may be fairly dehabilitating. To heal sprained legs, rest and ice packs may be all you need.\n For torn muscles, surgery or other medical attention may be necessary.\n\n Below are a couple of links leading to informational sites detailing how to spot these types of injuries.", font=("fixedsys", 14), anchor=CENTER)
    
        #mayoi = PhotoImage(file="Minnehack\\mayo.gif")
    mayo = Button(root, text='OrthoInfo (AAOS)')
    #mayo.image = mayoi
    new=1
    urlm = "https://orthoinfo.aaos.org/en/diseases--conditions/sprains-strains-and-other-soft-tissue-injuries/"
    def openmayo():
        webbrowser.open(urlm, new=new)
    mayo.config(command = openmayo)
    
    #clevelandi = PhotoImage(file="Minnehack\\mayo.gif")
    cleveland = Button(root, text='Mayo Clinic')
    #cleveland.image = clevelandi
    new=1
    urlc = "https://www.mayoclinic.org/symptoms/leg-pain/basics/causes/sym-20050784"
    def opencleveland():
        webbrowser.open(urlc, new=new)
    cleveland.config(command = opencleveland)
    
    cleveland.grid(row=2, column=1)
    mayo.grid(row=2, column=0)
    Info.grid(row=1, column=0, columnspan=2)
    bill.grid(row=0, column=0, columnspan=3)
    
def jointsc():
    global root, Upper_Body, Lower_body, Intro, bill, arms, legs, pelvis, tendonsligaments, muscles, feet, joints
    pelvis.destroy()
    legs.destroy()
    bill.destroy()
    joints.destroy()
    feet.destroy()
    tendonsligaments.destroy()
    muscles.destroy()
    
    bill = Label(text = 'Sore or painful leg joints.', font=("fixedsys", 14), anchor=CENTER)
    
    Info = Label(root, text = "Your leg joints may experiece many of the issues other joints are suceptible to.\nOverextension, dislocation, and general wear and tear will all contribute to pains in your joints.\n Some of these ailments can seriously deaden your ability to move around freely. \n\n Below are a couple of links leading to informational sites detailing some info about these injuries.", font=("fixedsys", 14), anchor=CENTER)
    
        #mayoi = PhotoImage(file="Minnehack\\mayo.gif")
    mayo = Button(root, text='Mayo Clinic')
    #mayo.image = mayoi
    new=1
    urlm = "https://www.mayoclinic.org/medical-professionals/clinical-updates/orthopedic-surgery/reducing-the-risk-of-recurrent-patellar-instability-in-skeletally-immature-patients"
    def openmayo():
        webbrowser.open(urlm, new=new)
    mayo.config(command = openmayo)
    
    #clevelandi = PhotoImage(file="Minnehack\\mayo.gif")
    cleveland = Button(root, text='Also Mayo Clinic, But a different page')
    #cleveland.image = clevelandi
    new=1
    urlc = "https://www.mayoclinic.org/symptoms/hip-pain/basics/causes/sym-20050684"
    def opencleveland():
        webbrowser.open(urlc, new=new)
    cleveland.config(command = opencleveland)
    
    cleveland.grid(row=2, column=1)
    mayo.grid(row=2, column=0)
    Info.grid(row=1, column=0, columnspan=2)
    bill.grid(row=0, column=0, columnspan=3)
    
def tendonsligamentsc():
    #end of line
    global root, Upper_Body, Lower_body, Intro, bill, arms, legs, pelvis, tendonsligaments, muscles, feet, joints
    pelvis.destroy()
    legs.destroy()
    bill.destroy()
    joints.destroy()
    feet.destroy()
    tendonsligaments.destroy()
    muscles.destroy()
    
    bill = Label(text = 'Problems with tendons and ligaments.', font=("fixedsys", 14), anchor=CENTER)
    
    Info = Label(root, text = "There are many tendons and other stretchy bits in your legs, \n none more infamous than the ALC and MCL, devastating injuries \n which can put a person out of commission for a long while.\n By not over-straining yourself, you can avoid suffering from these issues yourself. \n\n Below are links to some pages about issues that may occur with the major tendons in your legs.", font=("fixedsys", 14), anchor=CENTER)
    
        #mayoi = PhotoImage(file="Minnehack\\mayo.gif")
    mayo = Button(root, text='Mayo Clinic')
    #mayo.image = mayoi
    new=1
    urlm = "https://www.mayoclinic.org/diseases-conditions/hamstring-injury/symptoms-causes/syc-20372985"
    def openmayo():
        webbrowser.open(urlm, new=new)
    mayo.config(command = openmayo)
    
    #clevelandi = PhotoImage(file="Minnehack\\mayo.gif")
    cleveland = Button(root, text='OrthoInfo (AAOS)')
    #cleveland.image = clevelandi
    new=1
    urlc = "https://orthoinfo.aaos.org/en/diseases--conditions/anterior-cruciate-ligament-acl-injuries/"
    def opencleveland():
        webbrowser.open(urlc, new=new)
    cleveland.config(command = opencleveland)
    
    cleveland.grid(row=2, column=1)
    mayo.grid(row=2, column=0)
    Info.grid(row=1, column=0, columnspan=2)
    bill.grid(row=0, column=0, columnspan=3)
    
def feetc():
    global root, Upper_Body, Lower_body, Intro, bill, arms, legs, pelvis, tendonsligaments, muscles, feet, joints, jointsa, ankles, toes, tendonsligamentsf
    #arms.destroy()
    tendonsligaments.destroy()
    bill.destroy()
    muscles.destroy()
    feet.destroy()
    #joints.destroy()
    joints.destroy()
    bill = Label(root, text = "Where on (or in) your Feet does it hurt?", font=("fixedsys", 14), anchor=CENTER)
    
    toesi = PhotoImage(file="Minnehack\\toes.gif")
    toes = Button(root, image=toesi)
    toes.image = toesi
    toes.config(command = toesc)
    
    anklesi = PhotoImage(file="Minnehack\\ankles.gif")
    ankles = Button(root, image=anklesi)
    ankles.image = anklesi
    ankles.config(command = anklesc)
    
    tendonsligamentsfi = PhotoImage(file="Minnehack\\tendonsligaments.gif")
    tendonsligamentsf = Button(root, image=tendonsligamentsfi)
    tendonsligamentsf.image = tendonsligamentsfi
    tendonsligamentsf.config(command = tendonsligamentsfc)
    
    tendonsligamentsf.grid(row=1, column=2)
    ankles.grid(row=1, column=1)
    toes.grid(row=1, column=0)
    bill.grid(row=0, column=0, columnspan=3)
    
def toesc():
    global root, Upper_Body, Lower_body, Intro, bill, arms, legs, pelvis, tendonsligaments, muscles, feet, joints, jointsa, ankles, toes, tendonsligamentsf
    tendonsligamentsf.destroy()
    toes.destroy()
    ankles.destroy()
    bill.destroy()
    bill = Label(text = 'Toes and some issues that can happen', font=("fixedsys", 14), anchor=CENTER)
    
    Info = Label(root, text = "Toes take an unfortunate amount of abuse due their use and position\n on our body. When bad things happen to these sometimes sensitive mini-appendages, \n it can be a rough experience. \n\n These links will lead you to some info about toe injuries.", font=("fixedsys", 14), anchor=CENTER)
    
        #mayoi = PhotoImage(file="Minnehack\\mayo.gif")
    mayo = Button(root, text='Mayo Clinic')
    #mayo.image = mayoi
    new=1
    urlm = "https://www.mayoclinic.org/diseases-conditions/broken-toe/symptoms-causes/syc-20370463"
    def openmayo():
        webbrowser.open(urlm, new=new)
    mayo.config(command = openmayo)
    
    #clevelandi = PhotoImage(file="Minnehack\\mayo.gif")
    cleveland = Button(root, text='British NHS')
    #cleveland.image = clevelandi
    new=1
    urlc = "https://www.nhs.uk/conditions/broken-toe/"
    def opencleveland():
        webbrowser.open(urlc, new=new)
    cleveland.config(command = opencleveland)
    
    cleveland.grid(row=2, column=1)
    mayo.grid(row=2, column=0)
    Info.grid(row=1, column=0, columnspan=2)
    bill.grid(row=0, column=0, columnspan=3)
    
def tendonsligamentsfc():
    global root, Upper_Body, Lower_body, Intro, bill, arms, legs, pelvis, tendonsligaments, muscles, feet, joints, jointsa, ankles, toes, tendonsligamentsf
    tendonsligamentsf.destroy()
    toes.destroy()
    ankles.destroy()
    bill.destroy()
    bill = Label(text = 'Tendons and ligaments (in your feet).', font=("fixedsys", 14), anchor=CENTER)
    
    Info = Label(root, text = "Ligaments and tedons in your feet are often sliding around each other,\n and may be visible on the outside of a foot depending on your body.\n\n The following links will have some information related to what you may see down there.", font=("fixedsys", 14), anchor=CENTER)
    
        #mayoi = PhotoImage(file="Minnehack\\mayo.gif")
    mayo = Button(root, text='ACFAS')
    #mayo.image = mayoi
    new=1
    urlm = "https://www.foothealthfacts.org/conditions/peroneal-tendon-injuries"
    def openmayo():
        webbrowser.open(urlm, new=new)
    mayo.config(command = openmayo)
    
    #clevelandi = PhotoImage(file="Minnehack\\mayo.gif")
    cleveland = Button(root, text='Cleveland Clinic')
    #cleveland.image = clevelandi
    new=1
    urlc = "https://my.clevelandclinic.org/health/diseases/15225-achilles-tendon-injury---including-achilles-tendinitis-and-achilles-tendon-rupture"
    def opencleveland():
        webbrowser.open(urlc, new=new)
    cleveland.config(command = opencleveland)
    
    cleveland.grid(row=2, column=1)
    mayo.grid(row=2, column=0)
    Info.grid(row=1, column=0, columnspan=2)
    bill.grid(row=0, column=0, columnspan=3)
    
def anklesc():
    global root, Upper_Body, Lower_body, Intro, bill, arms, legs, pelvis, tendonsligaments, muscles, feet, joints, jointsa, ankles, toes, tendonsligamentsf
    tendonsligamentsf.destroy()
    toes.destroy()
    ankles.destroy()
    bill.destroy()
    bill = Label(text = 'Ankles, and the problems they may have.', font=("fixedsys", 14), anchor=CENTER)
    
    Info = Label(root, text = "The ankle, being a heavy-use and heavy-load joint tends to be \nsuceptible to injury frequently. Those in high action sports in particular \nare at risk for rolling or dislocating this foundational joint.\n\n Below are come links detailing a couple of possible ankle injuries.", font=("fixedsys", 14), anchor=CENTER)
    
        #mayoi = PhotoImage(file="Minnehack\\mayo.gif")
    mayo = Button(root, text='British NHS')
    #mayo.image = mayoi
    new=1
    urlm = "https://www.nhs.uk/conditions/broken-ankle/"
    def openmayo():
        webbrowser.open(urlm, new=new)
    mayo.config(command = openmayo)
    
    #clevelandi = PhotoImage(file="Minnehack\\mayo.gif")
    cleveland = Button(root, text='Mayo Clinic')
    #cleveland.image = clevelandi
    new=1
    urlc = "https://www.mayoclinic.org/diseases-conditions/sprained-ankle/symptoms-causes/syc-20353225"
    def opencleveland():
        webbrowser.open(urlc, new=new)
    cleveland.config(command = opencleveland)
    
    cleveland.grid(row=2, column=1)
    mayo.grid(row=2, column=0)
    Info.grid(row=1, column=0, columnspan=2)
    bill.grid(row=0, column=0, columnspan=3)
    
def pelvisc():
    global root, Upper_Body, Lower_body, Intro, bill, arms, legs, pelvis, hips, tailbone, groin
    #arms.destroy()
    legs.destroy()
    bill.destroy()
    pelvis.destroy()
    bill = Label(root, text = "Where on (or in) your Pelvis does it hurt?", font=("fixedsys", 14), anchor=CENTER)
    
    hipsi = PhotoImage(file="Minnehack\\hips.gif")
    hips = Button(root, image=hipsi)
    hips.image = hipsi
    hips.config(command = hipsc)
    
    tailbonei = PhotoImage(file="Minnehack\\tailbone.gif")
    tailbone = Button(root, image=tailbonei)
    tailbone.image = tailbonei
    tailbone.config(command = tailbonec)
    
    groini = PhotoImage(file="Minnehack\\groin.gif")
    groin = Button(root, image=groini)
    groin.image = groini
    groin.config(command = groinc)
    
    groin.grid(row=1, column=2)
    tailbone.grid(row=1, column=1)
    hips.grid(row=1, column=0)
    bill.grid(row=0, column=0, columnspan=3)

def hipsc():
    #end of line
    global root, Upper_Body, Lower_body, Intro, bill, arms, legs, pelvis, tendonsligaments, muscles, feet, joints, jointsa, ankles, toes, tendonsligamentsf, hips, tailbone, groin
    tailbone.destroy()
    groin.destroy()
    hips.destroy()
    bill.destroy()
    bill = Label(text = 'Hips, and the problems they may have.', font=("fixedsys", 14), anchor=CENTER)
    
    Info = Label(root, text = "Hips are the gateway to movement, and are tough jonts.\n Every once in a while they fail, and when it happens you know it.\n Hips can become dislocated, or begin to rub bone-on-bone which causes great amounts of pain. \n\nHere are a couple of links about hip dislocation and fracture, respectively.", font=("fixedsys", 14), anchor=CENTER)
    
        #mayoi = PhotoImage(file="Minnehack\\mayo.gif")
    mayo = Button(root, text='Mayo Clinic')
    #mayo.image = mayoi
    new=1
    urlm = "https://www.mayoclinic.org/diseases-conditions/hip-dysplasia/symptoms-causes/syc-20350209"
    def openmayo():
        webbrowser.open(urlm, new=new)
    mayo.config(command = openmayo)
    
    #clevelandi = PhotoImage(file="Minnehack\\mayo.gif")
    cleveland = Button(root, text='Cleaveland Clinic')
    #cleveland.image = clevelandi
    new=1
    urlc = "https://my.clevelandclinic.org/health/diseases/17101-hip-fracture"
    def opencleveland():
        webbrowser.open(urlc, new=new)
    cleveland.config(command = opencleveland)
    
    cleveland.grid(row=2, column=1)
    mayo.grid(row=2, column=0)
    Info.grid(row=1, column=0, columnspan=2)
    bill.grid(row=0, column=0, columnspan=3)
    
def tailbonec():
    global root, Upper_Body, Lower_body, Intro, bill, arms, legs, pelvis, tendonsligaments, muscles, feet, joints, jointsa, ankles, toes, tendonsligamentsf, hips, tailbone, groin
    tailbone.destroy()
    groin.destroy()
    hips.destroy()
    bill.destroy()
    bill = Label(text = 'The tailbone and why it is mostly just annoying.', font=("fixedsys", 14), anchor=CENTER)
    
    Info = Label(root, text = "The great majority of humans lack tails.\n Most people do have a tailbone though. It mostly stays \nout of the way until it doesn't and we bruise or break it unintentionally. \n\nThe two sites below have some information which may help you care for your bruised or broken coccyx.", font=("fixedsys", 14), anchor=CENTER)
    
        #mayoi = PhotoImage(file="Minnehack\\mayo.gif")
    mayo = Button(root, text='Mayo Clinic')
    #mayo.image = mayoi
    new=1
    urlm = "https://www.mayoclinic.org/tailbone-pain/expert-answers/faq-20058211"
    def openmayo():
        webbrowser.open(urlm, new=new)
    mayo.config(command = openmayo)
    
    #clevelandi = PhotoImage(file="Minnehack\\mayo.gif")
    cleveland = Button(root, text='US National Library of Medicine')
    #cleveland.image = clevelandi
    new=1
    urlc = "https://medlineplus.gov/ency/patientinstructions/000573.htm"
    def opencleveland():
        webbrowser.open(urlc, new=new)
    cleveland.config(command = opencleveland)
    
    cleveland.grid(row=2, column=1)
    mayo.grid(row=2, column=0)
    Info.grid(row=1, column=0, columnspan=2)
    bill.grid(row=0, column=0, columnspan=3)
    #end of line
    
def groinc():
    #end of line
    global root, Upper_Body, Lower_body, Intro, bill, arms, legs, pelvis, tendonsligaments, muscles, feet, joints, jointsa, ankles, toes, tendonsligamentsf, hips, tailbone, groin
    tailbone.destroy()
    groin.destroy()
    hips.destroy()
    bill.destroy()
    bill = Label(text = 'Groin injuries suck, but your actions can help.', font=("fixedsys", 14), anchor=CENTER)
    
    Info = Label(root, text = "A torn or herniated groin is a terrible experience.\n The area between our legs contains lots of nerves, \nand pulling or tearing anything can be a horrifying experience.\n\n These sites will give you some tips on how to care for or avoid a damaged groin.", font=("fixedsys", 14), anchor=CENTER)
    
        #mayoi = PhotoImage(file="Minnehack\\mayo.gif")
    mayo = Button(root, text='Mayo Clinic')
    #mayo.image = mayoi
    new=1
    urlm = "https://www.mayoclinic.org/diseases-conditions/inguinal-hernia/symptoms-causes/syc-20351547"
    def openmayo():
        webbrowser.open(urlm, new=new)
    mayo.config(command = openmayo)
    
    #clevelandi = PhotoImage(file="Minnehack\\mayo.gif")
    cleveland = Button(root, text='US National Library of Medicine')
    #cleveland.image = clevelandi
    new=1
    urlc = "https://www.ncbi.nlm.nih.gov/pubmedhealth/PMH0089666/"
    def opencleveland():
        webbrowser.open(urlc, new=new)
    cleveland.config(command = opencleveland)
    
    cleveland.grid(row=2, column=1)
    mayo.grid(row=2, column=0)
    Info.grid(row=1, column=0, columnspan=2)
    bill.grid(row=0, column=0, columnspan=3)

"""
#################################################################################
Everything above this is functions called essentially in a tree.

Everything below this is just for the start of the program

#################################################################################
"""

Intro = Label(root, text = "Click on the button describing where the pain is.", font=("fixedsys", 14), anchor=CENTER)

U_image = PhotoImage(file="Minnehack\\upper_body.gif")
Upper_Body = Button(root, image=U_image)
Upper_Body.image = U_image
Upper_Body.config(command = UBC)

L_image = PhotoImage(file="Minnehack\\lower_body.gif")
Lower_Body = Button(root, image=L_image)
Lower_Body.image = L_image
Lower_Body.config(command = LBC)

Intro.grid(row=0, column=0, columnspan=2)
Upper_Body.grid(row=1, column=0)
Lower_Body.grid(row=1, column=1)
root.update()