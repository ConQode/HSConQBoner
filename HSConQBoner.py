import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import Entry

# Global variables
opened_image_path = ""
sliders_data = []
image_path = ""  # Define the image_path globally
entry_widgets = []
initial_slider_values = {}
manual_entry_widgets = []  # List to store manual input entry widgets
slider_frame = None  # Store the frame containing sliders globally
sliders = []  # Initialize the sliders list
x_slider_vars = []  # Initialize x_slider_vars list
y_slider_vars = []  # Initialize y_slider_vars list
z_slider_vars = []  # Initialize z_slider_vars list
slider_labels = []  # Initialize the slider_labels list
min_slider_limit = 0.0
max_slider_limit = 2.0

root = tk.Tk()
root.title("HSConQBoner V1.05")
root.wm_attributes("-topmost", 1)  # Set the window to always be on top

# Additional names for bones
slider_name_mapping = {
    " cf_J_hairBL_00": "BlaTest1",
    " cf_J_hairBL_00": "",
    "cf_J_hairBR_00": "",
    "cf_hairB": "",
    "cf_hairB_top": "",
    "cf_hairBL_00": "",
    "cf_hairBR_00": "",
    "cf_hairF": "",
    "cf_hairS": "Side Hair",
    "cf_hit_Kosi02_s": "Hitbox - Hips",
    "cf_hit_LegUp01_s_L": "Hitbox - Thigh (L)",
    "cf_hit_LegUp01_s_R": "Hitbox - Thigh (R)",
    "cf_hit_Mune02_s_L": "Hitbox - Breast (L)",
    "cf_hit_Mune02_s_R": "Hitbox - Breast (R)",
    "cf_hit_Siri_s_L": "Hitbox - Butt (L)",
    "cf_hit_Siri_s_R": "Hitbox - Butt (R)",
    "cf_J_Ana": "Anus",
    "cf_J_ArmElbo_low_s_L": "Elbow (L)",
    "cf_J_ArmElbo_low_s_R": "Elbow (R)",
    "cf_J_ArmElboura_dam_L": "",
    "cf_J_ArmElboura_dam_R": "",
    "cf_J_ArmLow01_L": "Forearm (L)",
    "cf_J_ArmLow01_R": "Forearm (R)",
    "cf_J_ArmLow01_s_L": "Upper Forearm Tone (L)",
    "cf_J_ArmLow01_s_R": "Upper Forearm Tone (R)",
    "cf_J_ArmLow02_s_L": "Lower Forearm Tone (L)",
    "cf_J_ArmLow02_s_R": "Lower Forearm Tone (L)",
    "cf_J_ArmUp00_L": "Overall Arm (L)",
    "cf_J_ArmUp00_R": "Overall Arm (R)",
    "cf_J_ArmUp01_s_L": "Upper Humerus (L)",
    "cf_J_ArmUp01_s_R": "Lower Humerus (R)",
    "cf_J_ArmUp02_s_L": "Upper Humerus (L)",
    "cf_J_ArmUp02_s_R": "Lower Humerus (R)",
    "cf_J_ArmUp03_s_L": "Upper Humerus (L)",
    "cf_J_ArmUp03_s_R": "Lower Humerus (R)",
    "cf_J_CheekLow_L": "Lower Cheek (L)",
    "cf_J_CheekLow_R": "Lower Cheek (R)",
    "cf_J_CheekUp_L": "Upper Cheek (L)",
    "cf_J_CheekUp_R": "Upper Cheek (R)",
    "cf_J_Chin_rs ": "Jaw",
    "cf_J_ChinLow ": "",
    "cf_J_ChinTip_s": "Chin",
    "cf_J_EarBase_s_L": "Overall Ear (L)",
    "cf_J_EarBase_s_R": "Overall Ear (R)",
    "cf_J_EarLow_L": "Lower Ear (L)",
    "cf_J_EarLow_R": "Lower Ear (R)",
    "cf_J_EarRing_L": "Earring (L)",
    "cf_J_EarRing_R": "Earring (R)",
    "cf_J_EarUp_L": "Upper Ear (L)",
    "cf_J_EarUp_R": "Upper Ear (R)",
    "cf_J_Eye_r_L": "Eye (L)",
    "cf_J_Eye_r_R": "Eye (R)",
    "cf_J_eye_rs_L": "Eyeball (L)",
    "cf_J_eye_rs_R": "Eyeball (R)",
    "cf_J_Eye_s_L": "Overall Eye 1 (L)",
    "cf_J_Eye_s_R": "Overall Eye 1 (R)",
    "cf_J_Eye_t_L": "Overall Eye 2 (L)",
    "cf_J_Eye_t_R": "Overall Eye 2 (R)",
    "cf_J_Eye01_L": "Eyelid 1 (L)",
    "cf_J_Eye01_R": "Eyelid 1 (R)",
    "cf_J_Eye01_s_L": "",
    "cf_J_Eye01_s_R": "",
    "cf_J_Eye02_L": "Upper Eyelid (L)",
    "cf_J_Eye02_R": "Upper Eyelid (R)",
    "cf_J_Eye02_s_L": "",
    "cf_J_Eye02_s_R": "",
    "cf_J_Eye03_L": "Eyelid Outer Corner (L)",
    "cf_J_Eye03_R": "Eyelid Outer Corner (R)",
    "cf_J_Eye03_s_L": "",
    "cf_J_Eye03_s_R": "",
    "cf_J_Eye04_L": "Lower Eyelid (L)",
    "cf_J_Eye04_R": "Lower Eyelid (R)",
    "cf_J_Eye04_s_L": "",
    "cf_J_Eye04_s_R": "",
    "cf_J_EyePos_rz_L": "Eyeball (L)",
    "cf_J_EyePos_rz_R": "Eyeball (R)",
    "cf_J_FaceBase": "Overall Face",
    "cf_J_FaceLow_s": "Lower Face",
    "cf_J_FaceLowBase": "Lower Face Tone",
    "cf_J_FaceUp_ty": "Upper Face",
    "cf_J_FaceUp_tz": "Upper Face Tone",
    "cf_J_Foot01_L": "Foot & Ankle (L)",
    "cf_J_Foot01_R": "Foot & Ankle (R)",
    "cf_J_Foot02_L": "Foot (L)",
    "cf_J_Foot02_R": "Foot (R)",
    "cf_j_hair_camp1_F_L_2": "",
    "cf_j_hair_camp1_F_R_2": "",
    "cf_J_hairB": "",
    "cf_J_hairB_00": "",
    "cf_J_hairB_s": "",
    "cf_J_hairB_top": "Hair Top",
    "cf_J_hairB_twin_L_00": "",
    "cf_J_hairB_twin_R_00": "",
    "cf_J_hairBC_00": "",
    "cf_J_hairBC_01": "",
    "cf_J_hairBC_02": "",
    "cf_J_hairBC_03": "",
    "cf_J_hairBC_04": "",
    "cf_J_hairBC_05": "",
    "cf_J_hairBC_s": "Back Hair (M)",
    "cf_J_hairBL_00": "",
    "cf_J_hairBL_01": "",
    "cf_J_hairBL_02": "",
    "cf_J_hairBL_03": "",
    "cf_J_hairBL_s": "Pigtails (L)",
    "cf_J_hairBR_00": "",
    "cf_J_hairBR_01": "",
    "cf_J_hairBR_02": "",
    "cf_J_hairBR_03": "",
    "cf_J_hairBR_s": "Pigtails (R)",
    "cf_J_hairF": "",
    "cf_J_hairF_00": "",
    "cf_J_hairF_01": "",
    "cf_J_hairF_s": "",
    "cf_J_hairF_top": "Bangs",
    "cf_J_hairFC_s": "Bangs (M)",
    "cf_J_hairFL_00": "",
    "cf_J_hairFL_01": "",
    "cf_J_hairFL_02": "",
    "cf_J_hairFL_s": "Bangs (L)",
    "cf_J_hairFL00": "",
    "cf_J_hairFL01": "",
    "cf_J_hairFR_00": "",
    "cf_J_hairFR_01": "",
    "cf_J_hairFR_02": "",
    "cf_J_hairFR_s": "Bangs (R)",
    "cf_J_hairFSL_00": "",
    "cf_J_hairFSL_01": "",
    "cf_J_hairFSL_02": "",
    "cf_J_hairFSL_s": "",
    "cf_J_hairFSR_00": "",
    "cf_J_hairFSR_01": "",
    "cf_J_hairFSR_02": "",
    "cf_J_hairFSR_s": "",
    "cf_J_hairS": "Side Hair",
    "cf_J_hairS_top": "Side Hair",
    "cf_J_hairSL_00": "",
    "cf_J_hairSL_01": "",
    "cf_J_hairSL_02": "",
    "cf_J_hairSL_s": "",
    "cf_J_hairSR_00": "",
    "cf_J_hairSR_01": "",
    "cf_J_hairSR_02": "",
    "cf_J_hairSR_s": "",
    "cf_J_Hand_index01_L": "",
    "cf_J_Hand_Index01_L": "",
    "cf_J_Hand_index01_R": "",
    "cf_J_Hand_Index01_R": "",
    "cf_J_Hand_L": "Hand & Wirst (L)",
    "cf_J_Hand_Little01_L": "",
    "cf_J_Hand_Little01_R": "",
    "cf_J_Hand_Middle01_L": "",
    "cf_J_Hand_Middle01_R": "",
    "cf_J_Hand_R": "Hand & Wirst (R)",
    "cf_J_Hand_Ring01_L": "",
    "cf_J_Hand_Ring01_R": "",
    "cf_J_Hand_s_L": "Hand (L)",
    "cf_J_Hand_s_R": "Hand (R)",
    "cf_J_Hand_Thumb01_L": "",
    "cf_J_Hand_Thumb01_R": "",
    "cf_J_Hand_Wrist_s_L": "Wirst (L)",
    "cf_J_Hand_Wrist_s_R": "Wirst (R)",
    "cf_J_Head": "Head Scale",
    "cf_J_Head_s": "Overall Head",
    "cf_J_Hips": "Scale",
    "cf_J_Kokan": "Pussy",
    "cf_J_Kosi01": "Waist & Below",
    "cf_J_Kosi01_s": "Pelvis (no skirt)",
    "cf_J_Kosi02": "Hips & Below",
    "cf_J_Kosi02_s": "Hips (no skirt)",
    "cf_J_Kosi03": "",
    "cf_J_Kosi03_s": "",
    "cf_J_LegKnee_back_s_L": "Back of Knee (L)",
    "cf_J_LegKnee_back_s_R": "Back of Knee (R)",
    "cf_J_LegKnee_dam_L": "Front of Knee (L)",
    "cf_J_LegKnee_dam_R": "Front of Knee (R)",
    "cf_J_LegKnee_low_s_L": "Knee Tone (L)",
    "cf_J_LegKnee_low_s_R": "Knee Tone (R)",
    "cf_J_LegLow01_L": "Knees & Below",
    "cf_J_LegLow01_R": "Knees & Below",
    "cf_J_LegLow01_s_L": "Calf (L)",
    "cf_J_LegLow01_s_R": "Calf (R)",
    "cf_J_LegLow02_s_L": "Lower Calf (L)",
    "cf_J_LegLow02_s_R": "Lower Calf (R)",
    "cf_J_LegLow03_s_L": "Ankle (L)",
    "cf_J_LegLow03_s_R": "Ankle (R)",
    "cf_J_LegLowRoll_L": "Lower Leg Length (L)",
    "cf_J_LegLowRoll_R": "Lower Leg Length (R)",
    "cf_J_LegUp00_L": "Overall Leg (L)",
    "cf_J_LegUp00_R": "Overall Leg (R)",
    "cf_J_LegUp01_s_L": "Upper Thigh (L)",
    "cf_J_LegUp01_s_R": "Upper Thigh (R)",
    "cf_J_LegUp02_s_L": "Lower Thigh (L)",
    "cf_J_LegUp02_s_R": "Lower Thigh (R)",
    "cf_J_LegUp03_L": "Knee (L)",
    "cf_J_LegUp03_R": "Knee (R)",
    "cf_J_LegUp03_s_L": "Above the Knee (L)",
    "cf_J_LegUp03_s_R": "Above the Knee (R)",
    "cf_J_LegUpDam_L": "Upper Hip (L)",
    "cf_J_LegUpDam_R": "Upper Hip (R)",
    "cf_J_LegUpDam_s_L": "Upper Hip (L)",
    "cf_J_LegUpDam_s_R": "Upper Hip (R)",
    "cf_J_LegUpRoll_L": "",
    "cf_J_LegUpRoll_R": "",
    "cf_J_look_L": "",
    "cf_J_look_R": "",
    "cf_J_Mayu_L": "Eyebrow (L)",
    "cf_J_Mayu_R": "Eyebrow (R)",
    "cf_J_MayuMid_s_L": "Eyebrow Middle (L)",
    "cf_J_MayuMid_s_R": "Eyebrow Middle (R)",
    "cf_J_MayuTip_L": "",
    "cf_J_MayuTip_s_L": "Eyebrow End (L)",
    "cf_J_MayuTip_s_R": "Eyebrow End (R)",
    "cf_J_megane": "Glasses",
    "cf_J_Mouth_L": "Mouth (L)",
    "cf_J_Mouth_R": "Mouth (R)",
    "cf_J_MouthBase_s": "Lips",
    "cf_J_MouthBase_tr": "Mouth (with teeth)",
    "cf_J_MouthCavity": "Teeth",
    "cf_J_MouthLow": "Lower Lip Tone",
    "cf_J_Mouthup": "Upper Lip Tone",
    "cf_J_MouthUp": "",
    "cf_J_Mune_Nip01_L": "",
    "cf_J_Mune_Nip01_R": "",
    "cf_J_Mune_Nip01_s_L": "Nipple (L)",
    "cf_J_Mune_Nip01_s_R": "Nipple (R)",
    "cf_J_Mune_Nip02_s_L": "Nipple Tip (L)",
    "cf_J_Mune_Nip02_s_R": "Nipple Tip (R)",
    "cf_J_Mune_Nipacs01_L": "",
    "cf_J_Mune_Nipacs01_R": "",
    "cf_J_Mune00": "",
    "cf_J_Mune00_d_L": "Middle part of Breast (L)",
    "cf_J_Mune00_d_R": "Middle part of Breast (R)",
    "cf_J_Mune00_s_L": "Breast Closest to Chest (L)",
    "cf_J_Mune00_s_R": "Breast Closest to Chest (R) ",
    "cf_J_Mune00_t_L": "Outer part of Breast (L)",
    "cf_J_Mune00_t_R": "Outer part of Breast (R)",
    "cf_J_Mune01_s_L": "Middle of Breast (L)",
    "cf_J_Mune01_s_R": "Middle of Breast (R)",
    "cf_J_Mune01_t_L": "Outer part of Breast (L)",
    "cf_J_Mune01_t_R": "Outer part of Breast (R)",
    "cf_J_Mune02_s_L": "Outer part of Breast (L)",
    "cf_J_Mune02_s_R": "Outer part of Breast (R)",
    "cf_J_Mune02_t_L": "Tip of Breast (L)",
    "cf_J_Mune02_t_R": "Tip of Breast (R)",
    "cf_J_Mune03_s_L": "Tip of Breast (L)",
    "cf_J_Mune03_s_R": "Tip of Breast (R)",
    "cf_J_Mune04_s_L": "Areola (L)",
    "cf_J_Mune04_s_R": "Areola (R)",
    "cf_J_Neck": "Head & Neck",
    "cf_J_Neck_s": "Neck [Don't Use]",
    "cf_J_Nose_t": "Upper Nose",
    "cf_J_Nose_tip": "Nose Tip",
    "cf_J_NoseBase_s": "Nose",
    "cf_J_NoseBase_trs": "Nose & Bridge",
    "cf_J_NoseBridge_s": "Bridge",
    "cf_J_NoseBridge_t": "Bridge",
    "cf_J_NoseWing_tx_L": "Nostril (L)",
    "cf_J_NoseWing_tx_R": "Nostril (R)",
    "cf_J_pupil_s_L": "Pupil (L)",
    "cf_J_pupil_s_R": "Pupil (R)",
    "cf_J_Root": "Scale of Character",
    "cf_J_Shoulder_L": "Shoulder & Arm Scale (L)",
    "cf_J_Shoulder_R": "Shoulder & Arm Scale (R)",
    "cf_J_Shoulder02_s_L": "Shoulder Tone (L)",
    "cf_J_Shoulder02_s_R": "Shoulder Tone (R)",
    "cf_J_ShoulderIK_L": "Arm Length & Shoulder Elevation (L)",
    "cf_J_ShoulderIK_R": "Arm Length & Shoulder Elevation (R)",
    "cf_J_Siri_s_L": "Overall Butt (L)",
    "cf_J_Siri_s_R": "Overall Butt (R)",
    "cf_J_SiriDam_L": "Overall Butt/Butt Tone (L) (no skirt)",
    "cf_J_SiriDam_R": "Overall Butt/Butt Tone (R) (no skirt)",
    "cf_J_SiriDam01_L": "Butt (L)",
    "cf_J_SiriDam01_R": "Butt (R)",
    "cf_J_Siriopen_s_L": "Butt Apart (L)",
    "cf_J_Siriopen_s_R": "Butt Apart (R)",
    "cf_J_sk_00_00_dam": "Front of Skirt (M)",
    "cf_J_sk_01_00_dam": "Front of Skirt (R)",
    "cf_J_sk_02_00_dam": "Side of Skirt (R)",
    "cf_J_sk_03_00_dam": "Back of Skirt (R)",
    "cf_J_sk_04_00_dam": "Back of Skirt (M)",
    "cf_J_sk_05_00_dam": "Back of Skirt (L)",
    "cf_J_sk_06_00_dam": "Side of Skirt (L)",
    "cf_J_sk_07_00_dam": "Front of Skirt (L)",
    "cf_J_sk_siri_dam": "Back of Skirt",
    "cf_J_sk_top": "Overall Skirt",
    "cf_J_Spine01": "Waist & Above",
    "cf_J_Spine01_s": "Waist",
    "cf_J_Spine02": "Ribcage & Above",
    "cf_J_Spine02_s": "",
    "cf_J_Spine03": "Neck Delta & Above",
    "cf_J_Spine03_s": "",
    "cf_J_Tang_S_02_at": "",
    "cf_J_Toes01_L": "Toes (L)",
    "cf_J_Toes01_R": "Toes (R)",
    "cf_N_height": "Height",
    "cf_N_J_hairback_16": "",
    "cf_N_J_hairback_92": "",
    "cf_N_J_hairback_ph01": "",
    "cf_N_J_hairback_ph04": "",
    "cf_N_J_hairfront_91": "",
    "cf_o_mayuge": "",
    "ChinLow": "",
    "cm_J_Kosi01": "",
    "f_J_hairF_top": "",
    "hairB_top": "",
    "N_hairback92": "",
    "N_hairfront83": "",
    "cm_J_dan": "Penis and Balls",
    "cm_J_dan100_00": "Penis",
    "cm_J_dan_f_top": "Balls",
    "cm_J_dan_f_L": "Left Nut",
    "cm_J_dan_f_R": "Right Nut"
}


def update_slider_limits():
    global min_slider_limit, max_slider_limit

    # Get the values from the Entry widgets
    min_limit = min_limit_entry.get()
    max_limit = max_limit_entry.get()

    # Validate and update the limits
    if min_limit:
        min_slider_limit = float(min_limit)
    if max_limit:
        max_slider_limit = float(max_limit)

    # Update the scales of the sliders
    for slider in sliders:
        slider[0].config(from_=min_slider_limit)
        slider[0].config(to=max_slider_limit)
        slider[1].config(from_=min_slider_limit)
        slider[1].config(to=max_slider_limit)
        slider[2].config(from_=min_slider_limit)
        slider[2].config(to=max_slider_limit)



# Function to create the scrollbar
def create_scrollbar():
    global sidebar_scrollbar

    sidebar_scrollbar = tk.Scrollbar(sidebar_frame, orient=tk.VERTICAL, command=sidebar_canvas.yview)
    sidebar_scrollbar.grid(row=0, column=1, sticky="ns")  # Use grid for sidebar_scrollbar
    sidebar_canvas.configure(yscrollcommand=sidebar_scrollbar.set)

# Function to filter sliders based on user input
def filter_sliders(event=None):
    filter_text = filter_entry.get().lower()

    # Clear the slider frame
    for widget in slider_container.winfo_children():  # Use slider_container instead of slider_frame
        widget.grid_remove()

    # Track the number of visible sliders
    visible_sliders = 0

    for i, label in enumerate(slider_labels):
        # Check if the filter text is in lowercase and is present in the lowercase slider label
        if filter_text and filter_text in label.cget("text").lower():
            # Show the slider if it matches the filter
            for item in sliders[i]:
                item.grid()
            label.grid()
            for j in range(i * 3, i * 3 + 3):
                entry_widgets[j].grid()  # Show the entry fields for manual inputs
            visible_sliders += 1

    # Update the canvas size based on the number of visible sliders
    canvas.config(scrollregion=canvas.bbox("all"))

    # Update the scrollbar for the slider frame
    slider_container.update_idletasks()
    sidebar_canvas.config(scrollregion=sidebar_canvas.bbox("all"))

    
# Function to open a .png file and display it
def open_image():
    global opened_image_path, sliders_data, image_path

    file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    if file_path:
        opened_image_path = file_path
        image_path = file_path  # Set the image_path here
        image_label.config(text="")  # Update the text with your custom message

        # Clear existing values, sliders, and entry fields
        clear_existing_sliders()

        load_image_preview(file_path)
        load_values_from_txt(file_path)
           
def clear_existing_sliders():
    global sliders_data, x_slider_vars, y_slider_vars, z_slider_vars, slider_labels, entry_widgets

    # Clear any existing sliders and manual input entry widgets
    for slider in sliders:
        slider[0].destroy()
        slider[1].destroy()
        slider[2].destroy()
    for entry_widget in entry_widgets:
        entry_widget.destroy()

    sliders.clear()
    x_slider_vars.clear()
    y_slider_vars.clear()
    z_slider_vars.clear()
    slider_labels.clear()
    entry_widgets.clear()

    # Clear the sliders_data dictionary
    sliders_data.clear()

    # Clear the initial_slider_values dictionary
    initial_slider_values.clear()

    # Clear the canvas image
    canvas.delete("all")

def load_image_preview(image_path):
    image = Image.open(image_path)
    image.thumbnail((260, 360))  # Resize the image for preview
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(130, 180, anchor=tk.CENTER, image=photo)
    canvas.image = photo  # Keep a reference to prevent garbage collection

# Function to load values from the .txt file and update sliders
def load_values_from_txt(image_path):
    global sliders_data, x_slider_vars, y_slider_vars, z_slider_vars, slider_labels, initial_slider_values
    global min_slider_limit, max_slider_limit

    txt_file = image_path + ".bonemod.txt"

    try:
        with open(txt_file, "r") as f:
            sliders_data = [line.strip().split(",") for line in f]

        # Determine the minimum and maximum values from the loaded file
        loaded_min_value = min(float(data[3]) for data in sliders_data)
        loaded_max_value = max(float(data[3]) for data in sliders_data)

        # Update Min Limit and Max Limit based on loaded values
        min_slider_limit = min(min_slider_limit, loaded_min_value)
        max_slider_limit = max(max_slider_limit, loaded_max_value)

        # Create sliders dynamically based on the number of lines in the .txt file
        num_sliders = len(sliders_data)
        create_sliders(num_sliders)

        for i, data in enumerate(sliders_data):
            x_value = float(data[3])
            y_value = float(data[4])
            z_value = float(data[5])

            # Get the slider name from the loaded data
            slider_name = data[1]

            # Check if there is a custom name in the mapping dictionary
            custom_name = slider_name_mapping.get(slider_name, "")

            # Set slider label text to the custom name appended to the original name (if custom_name is not empty)
            if custom_name:
                slider_labels[i].config(text=f"{slider_name}\n({custom_name})")
            else:
                slider_labels[i].config(text=slider_name)

            # Set slider values
            x_slider_vars[i].set(x_value)
            y_slider_vars[i].set(y_value)
            z_slider_vars[i].set(z_value)

            # Store initial slider values in the dictionary
            initial_slider_values[i] = {"x": x_value, "y": y_value, "z": z_value}

        # Update the slider limits after loading values
        update_slider_limits()
    except FileNotFoundError:
        print(f"Warning: {txt_file} not found.")


        
# Function to update slider labels based on the custom mapping dictionary
def update_slider_labels():
    global slider_labels

    for i, data in enumerate(sliders_data):
        # Get the slider name from the loaded data
        slider_name = data[1]

        # Check if there is a custom name in the mapping dictionary
        custom_name = slider_name_mapping.get(slider_name, slider_name)

        # Set slider label text to the custom name
        slider_labels[i].config(text=custom_name)

# Function to create sliders dynamically based on the number of lines
def create_sliders(num_sliders):
    global sliders, x_slider_vars, y_slider_vars, z_slider_vars, slider_labels, entry_widgets

    # Create sliders based on the number of lines
    for i in range(num_sliders):
        label = tk.Label(slider_container, text=f"Slider {i + 1}")
        label.grid(row=i, column=0)

        x_slider_var = tk.DoubleVar()
        y_slider_var = tk.DoubleVar()
        z_slider_var = tk.DoubleVar()

        x_slider = tk.Scale(slider_container, from_=min_slider_limit, to=max_slider_limit, resolution=0.01, orient=tk.HORIZONTAL, variable=x_slider_var)
        x_slider.grid(row=i, column=1)
        y_slider = tk.Scale(slider_container, from_=min_slider_limit, to=max_slider_limit, resolution=0.01, orient=tk.HORIZONTAL, variable=y_slider_var)
        y_slider.grid(row=i, column=2)
        z_slider = tk.Scale(slider_container, from_=min_slider_limit, to=max_slider_limit, resolution=0.01, orient=tk.HORIZONTAL, variable=z_slider_var)
        z_slider.grid(row=i, column=3)

        entry_x = Entry(slider_container, textvariable=x_slider_var, width=6)
        entry_x.grid(row=i, column=4)
        entry_y = Entry(slider_container, textvariable=y_slider_var, width=6)
        entry_y.grid(row=i, column=5)
        entry_z = Entry(slider_container, textvariable=z_slider_var, width=6)
        entry_z.grid(row=i, column=6)

        sliders.append((x_slider, y_slider, z_slider))
        x_slider_vars.append(x_slider_var)
        y_slider_vars.append(y_slider_var)
        z_slider_vars.append(z_slider_var)
        slider_labels.append(label)
        entry_widgets.extend([entry_x, entry_y, entry_z])

        # Bind slider changes to the update function
        x_slider.bind("<ButtonRelease-1>", update_txt_file)
        y_slider.bind("<ButtonRelease-1>", update_txt_file)
        z_slider.bind("<ButtonRelease-1>", update_txt_file)

        # Bind Enter key to entry fields to save
        entry_x.bind("<Return>", update_txt_file)
        entry_y.bind("<Return>", update_txt_file)
        entry_z.bind("<Return>", update_txt_file)

        # Bind FocusOut event to entry fields to save
        entry_x.bind("<FocusOut>", update_txt_file)
        entry_y.bind("<FocusOut>", update_txt_file)
        entry_z.bind("<FocusOut>", update_txt_file)

    # Update the scroll region of the sidebar canvas
    slider_container.update_idletasks()
    sidebar_canvas.config(scrollregion=sidebar_canvas.bbox("all"))

# Function to update the .txt file when slider values change
def update_txt_file(event=None):
    global sliders_data

    txt_file = image_path + ".bonemod.txt"

    for i in range(len(sliders_data)):
        x_value = x_slider_vars[i].get()
        y_value = y_slider_vars[i].get()
        z_value = z_slider_vars[i].get()

        # Check if the slider values have changed
        flag = "True" if x_value != 1.0 or y_value != 1.0 or z_value != 1.0 else "False"

        sliders_data[i] = [
            sliders_data[i][0],
            sliders_data[i][1],
            flag,
            str(x_value),
            str(y_value),
            str(z_value),
            str("1")
        ]

    with open(txt_file, "w") as f:
        for line in sliders_data:
            f.write(",".join(line) + "\n")

    print(f"Saved to {txt_file}")



# Create and configure widgets using grid layout
open_button = tk.Button(root, text="Open", command=open_image)
open_button.grid(row=0, column=0, columnspan=1, sticky="we", pady=5, padx=5)  # Centered and spans 2 columns

## Create a frame for the filter input and slider limits
filter_frame = tk.Frame(root)
filter_frame.grid(row=0, column=1, columnspan=5, sticky="we")  # Positioned at the top-left

image_label = tk.Label(root, text="")
image_label.grid(row=1, column=2, columnspan=2)
canvas = tk.Canvas(root, width=260, height=360)
canvas.grid(row=2, column=0, columnspan=4)


# Create labels and entry fields for both lower and upper slider limits
min_limit_label = tk.Label(filter_frame, text="Min Limit:")
min_limit_label.grid(row=0, column=2, sticky="we", padx=2)  # Position to the right of the filter
min_limit_entry = tk.Entry(filter_frame, width=5)
min_limit_entry.grid(row=0, column=3, sticky="we")  # Position to the right of the filter

max_limit_label = tk.Label(filter_frame, text="Max Limit:")
max_limit_label.grid(row=0, column=4, sticky="we", padx=2)  # Position to the right of the filter
max_limit_entry = tk.Entry(filter_frame, width=5)
max_limit_entry.grid(row=0, column=5, sticky="we")  # Position to the right of the filter

# Button to update the slider limits
update_limit_button = tk.Button(filter_frame, text="Update Limits", command=update_slider_limits)
update_limit_button.grid(row=0, column=6, sticky="e", padx=5)  # Position to the right of the filter



# Create a frame for the scrollable sidebar
sidebar_frame = tk.Frame(root)
sidebar_frame.grid(row=2, column=4, rowspan=12, sticky="ns")

# Create a canvas for the scrollable area in the sidebar
sidebar_canvas = tk.Canvas(sidebar_frame, width=700, height=360)
sidebar_canvas.grid(row=0, column=0, sticky="nsew")  # Use grid for sidebar_canvas

# Add a scrollbar to the sidebar and configure it
sidebar_scrollbar = tk.Scrollbar(sidebar_frame, orient=tk.VERTICAL, command=sidebar_canvas.yview)
sidebar_scrollbar.grid(row=0, column=1, sticky="ns")  # Use grid for sidebar_scrollbar
sidebar_canvas.configure(yscrollcommand=sidebar_scrollbar.set)

# Create a frame to contain the sliders in the sidebar canvas
slider_container = tk.Frame(sidebar_canvas)
sidebar_canvas.create_window((0, 0), window=slider_container, anchor=tk.NW)

# Initialize the slider_frame here
slider_frame = slider_container

# Create the "Save" button
save_button = tk.Button(root, text="Save", command=update_txt_file)
save_button.grid(row=14, column=0, columnspan=4, sticky="ew")  # Adjust the row

# Create a label for the filter
filter_label = tk.Label(filter_frame, text="Filter:")
filter_label.grid(row=0, column=7)  # Position to the right of the update button

# Entry field for the filter
filter_entry = tk.Entry(filter_frame)
filter_entry.grid(row=0, column=8)  # Position to the right of the filter label
filter_entry.bind("<KeyRelease>", filter_sliders)

# Start the tkinter main loop
root.mainloop()