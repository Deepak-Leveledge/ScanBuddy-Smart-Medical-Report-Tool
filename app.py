# import os
# from PIL import Image as PILImage
# from agno.agent import Agent
# from agno.models.google import Gemini
# import streamlit as st
# from agno.tools.duckduckgo import DuckDuckGoTools
# from agno.media import Image as AgnoImage
# import PyPDF2


# if "GOOGLE_API_KEY" not in st.session_state:
#     st.session_state.GOOGLE_API_KEY = None

# with st.sidebar:
#     st.title("ℹ️ Configuration")
    
#     if not st.session_state.GOOGLE_API_KEY:
#         api_key = st.text_input(
#             "Enter your Google API Key:",
#             type="password"
#         )
#         st.caption(
#             "Get your API key from [Google AI Studio]"
#             "(https://aistudio.google.com/apikey) 🔑"
#         )
#         if api_key:
#             st.session_state.GOOGLE_API_KEY = api_key
#             st.success("API Key saved!")
#             st.rerun()
#     else:
#         st.success("API Key is configured")
#         if st.button("🔄 Reset API Key"):
#             st.session_state.GOOGLE_API_KEY = None
#             st.rerun()
    
#     st.info(
#         "This tool provides AI-powered analysis of medical imaging data using "
#         "advanced computer vision and radiological expertise."
#     )
#     st.warning(
#         "⚠DISCLAIMER: This tool is for educational and informational purposes only. "
#         "All analyses should be reviewed by qualified healthcare professionals. "
#         "Do not make medical decisions based solely on this analysis."
#     )

# medical_agent = Agent(
#     model=Gemini(
#         id="gemini-2.0-flash",
#         api_key=st.session_state.GOOGLE_API_KEY
#     ),
#     tools=[DuckDuckGoTools()],
#     markdown=True
# ) if st.session_state.GOOGLE_API_KEY else None

# if not medical_agent:
#     st.warning("Please configure your API key in the sidebar to continue")

# # Medical Analysis Query
# query = """
# You are a highly skilled medical imaging expert with extensive knowledge in radiology and diagnostic imaging. Analyze the patient's medical image and structure your response as follows:

# ### 1. Image Type & Region
# - Specify imaging modality (X-ray/MRI/CT/Ultrasound/etc.)
# - Identify the patient's anatomical region and positioning
# - Comment on image quality and technical adequacy

# ### 2. Key Findings
# - List primary observations systematically
# - Note any abnormalities in the patient's imaging with precise descriptions
# - Include measurements and densities where relevant
# - Describe location, size, shape, and characteristics
# - Rate severity: Normal/Mild/Moderate/Severe

# ### 3. Diagnostic Assessment
# - Provide primary diagnosis with confidence level
# - List differential diagnoses in order of likelihood
# - Support each diagnosis with observed evidence from the patient's imaging
# - Note any critical or urgent findings

# ### 4. Patient-Friendly Explanation
# - Explain the findings in simple, clear language that the patient can understand
# - Avoid medical jargon or provide clear definitions
# - Include visual analogies if helpful
# - Address common patient concerns related to these findings

# ### 5. Research Context
# IMPORTANT: Use the DuckDuckGo search tool to:
# - Find recent medical literature about similar cases
# - Search for standard treatment protocols
# - Provide a list of relevant medical links of them too
# - Research any relevant technological advances
# - Include 2-3 key references to support your analysis

# Format your response using clear markdown headers and bullet points. Be concise yet thorough.
# """

# st.title("🏥 Medical Imaging Diagnosis Agent")
# st.write("Upload a medical image for professional analysis")

# # Create containers for better organization
# upload_container = st.container()
# image_container = st.container()
# analysis_container = st.container()

# with upload_container:
#     uploaded_file = st.file_uploader(
#         "Upload Medical Image",
#         type=["jpg", "jpeg", "png", "dicom","pdf"],
#         help="Supported formats: JPG, JPEG, PNG, DICOM ,PDF"
#     )

# if uploaded_file is not None:
#     with image_container:
#         col1, col2, col3 = st.columns([1, 2, 1])
#         with col2:
#             if uploaded_file.type in ["image/jpeg", "image/png", "image/gif", "image/bmp", "image/tiff"]:
#                 image = PILImage.open(uploaded_file)
#                 width, height = image.size
#                 aspect_ratio = width / height
#                 new_width = 500
#                 new_height = int(new_width / aspect_ratio)
#                 resized_image = image.resize((new_width, new_height))
                
#                 st.image(
#                     resized_image,
#                     caption="Uploaded Medical Image",
#                     use_container_width=True
#                 )
                
#                 analyze_button = st.button(
#                     "🔍 Analyze Image",
#                     type="primary",
#                     use_container_width=True
#                 )
#             elif uploaded_file.type == "application/pdf":
#                 pdf_file = PyPDF2.PdfReader(uploaded_file)
#                 text = ""
#                 for page in pdf_file.pages:
#                     text += page.extract_text()
#                 st.write("Uploaded PDF File:")
#                 st.write(text)
#                 analyze_button = st.button(
#                     "🔍 Analyze PDF",
#                     type="primary",
#                     use_container_width=True
#                 )
#             else:
#                 st.error("Only image and PDF files are supported. Please upload a valid file.")
#                 resized_image = None


#     with analysis_container:
#         if analyze_button:
#            with st.spinner("🔄 Analyzing... Please wait."):
#             try:
#                 if uploaded_file.type == "application/pdf":
#                     # PDF case: send extracted text to AI
#                     response = medical_agent.run(
#                         f"""You are a medical document analyst. Read and explain the following PDF report:
                        
# {text}

# Respond with structured diagnosis and patient-friendly explanation."""
#                     )
#                 else:
#                     # Image case
#                     temp_path = "temp_resized_image.png"
#                     resized_image.save(temp_path)
#                     agno_image = AgnoImage(filepath=temp_path)
#                     response = medical_agent.run(query, images=[agno_image])

#                 st.markdown("### 📋 Analysis Results")
#                 st.markdown("---")
#                 st.markdown(response.content)
#                 st.markdown("---")
#                 st.caption(
#                     "Note: This analysis is generated by AI and should be reviewed by "
#                     "a qualified healthcare professional."
#                 )
#             except Exception as e:
#                 st.error(f"Analysis error: {e}")

# else:
#     st.info("👆 Please upload a medical image to begin analysis")





import os
from PIL import Image as PILImage
from agno.agent import Agent
from agno.models.google import Gemini
import streamlit as st
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.media import Image as AgnoImage
import PyPDF2
from dotenv import load_dotenv
from io import BytesIO




# Load environment variables
load_dotenv()


# Get API key from environment variable
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# SESSION STATE INITIALIZATION - Adding more variables
# if "GOOGLE_API_KEY" not in st.session_state:
#     st.session_state.GOOGLE_API_KEY = None
if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "analyzed_file" not in st.session_state:
    st.session_state.analyzed_file = None

# SIDEBAR CONFIGURATION
with st.sidebar:
    st.title("ℹ️ ScanBuddy Analysis & Instructions")
    
    # API Status indicator
    if GOOGLE_API_KEY:
        st.success("API is configured and ready to use.")
    else:
        st.error("API key not found. Please check server configuration.")
        st.stop()  # Stop execution if API key is not found
    
    # Project information with expandable sections
    st.subheader("📚 About This Tool")
    st.info("This tool provides AI-powered analysis of medical imaging data using advanced computer vision and radiological expertise.")
    
    with st.expander("🎯 How to Use"):
        st.markdown("""
        **Step 1:** Upload an X-ray, MRI, CT scan, or a medical PDF report using the file uploader.
        
        **Step 2:** Click the "Analyze File" button to process your medical document.
        
        **Step 3:** View the detailed analysis in the "Analysis Results" tab to understand your report and "Download" the report If you want .
        
        **Step 4:** Ask questions about the report in the "Ask Questions" tab to better understand your results.
        """)
    
    with st.expander("✨ Benefits"):
        st.markdown("""
        - **Quick Analysis:** Get preliminary insights about medical images in minutes
        - **Language Simplification:** Complex medical terms explained in simple language
        - **Interactive Q&A:** Ask follow-up questions about your report
        - **Research Context:** Get information about similar cases and treatment options
        - **Accessibility:** Understand medical reports without waiting for appointments
        """)
    
    with st.expander("❓ Frequently Asked Questions"):
        st.markdown("""
        **Q: Is this a replacement for professional medical advice?**  
        A: No. This tool is for educational purposes only and should not replace consultation with healthcare professionals.
        
        **Q: What types of files can I analyze?**  
        A: You can upload JPG, PNG, JPEG, DICOM format medical images, or PDF medical reports.
        
        **Q: Is my data secure?**  
        A: Your uploaded files are processed temporarily and are not stored permanently. Your privacy is important to us.
        
        **Q: Can I download the analysis report?**  
        A: Currently, you can copy the analysis from the interface. Download functionality may be added in future updates.
        
        **Q: How accurate is the AI analysis?**  
        A: While the AI uses advanced models, it should be considered as a supplementary tool. Accuracy varies based on image quality and complexity.
        """)

    # ─── New “Questions & Suggestions” Section ────────────────────────────────────

    st.markdown("## 🙋 Questions & Suggestions")
    st.write(
        "If you have any questions, feedback or feature-requests, "
        "please drop us a line at "
        "[deepakleveledge@gmail.com](mailto:deepakleveledge@gmail.com). "
        "We’d love to hear your thoughts!"
    )

        
    
    st.warning("⚠️ DISCLAIMER: This tool is for educational and informational purposes only. Always consult a qualified healthcare professional for proper diagnosis and treatment.")



# AGENT SETUP
medical_agent = Agent(
    model=Gemini(id="gemini-2.0-flash", api_key=GOOGLE_API_KEY),
    tools=[DuckDuckGoTools()],
    markdown=True
) if GOOGLE_API_KEY else None

# PROMPT TEMPLATE FOR IMAGE ANALYSIS
query = """
Tum ek expert doctor ho jo X-ray, MRI, CT scan jaise images dekhkar diagnosis karte ho. Patient ne ek medical image bheja hai. Usko achhe se dekhkar niche ke steps follow karo:

### 1. Image Type & Body Part
- Yeh image kis type ka hai? (X-ray, MRI, CT scan, ultrasound, etc.)
- Patient ke body ka kaunsa part dikh raha hai?
- Image sahi se liya gaya hai ya nahi? Quality theek hai?

### 2. Main Findings
- Image me kya kya dikh raha hai? Point by point batao.
- Agar kuch abnormal ya galat dikh raha hai to clearly describe karo.
- Size, shape, location, density ya koi special feature mention karo.
- Har cheez ka severity level batao: Normal, Mild, Moderate ya Severe.

### 3. Doctor's Opinion (Diagnosis)
- Tumhara main diagnosis kya hai? Kitna confident ho usme?
- Agar kuch aur bimari bhi ho sakti hai to unke naam batao, most likely se least likely tak.
- Har diagnosis ke peeche reason bhi do — image me kya evidence mila hai.
- Agar koi urgent ya critical cheez ho to usko highlight karo.

### 4. Simple Language Explanation (For Patient)
- Sab kuch simple shabdon me explain karo jise patient samajh sake.
- Medical terms ka asaan matlab batao.
- Agar zarurat lage to example ya visual soch kar samjhao.
- Common doubts ya concerns bhi address karo.

### 5. Research & Links
- DuckDuckGo search tool ka use karke:
    - Similar cases ke baare me latest research dhoondo.
    - Standard treatment protocols kya hain vo batao.
    - 2–3 important and helpful links do jise user padh sakta hai.
    - Koi naye technology ya treatment ke baare me bhi info do.

Apna answer neat and clean markdown format me do, headings aur bullet points use karke. Short aur clear likho.
"""

# PROMPT FOR PDF FORMAT 
pdf_query = """
Tum ek experienced medical document expert ho. Neeche ek patient ka medical report diya gaya hai (PDF se nikala gaya text). Tumhara kaam hai:

1. Pura report dhyan se padhkar samjhao ki usme kya likha hai.
2. Patient ko simple words me samjhao ki report kya keh raha hai.
3. Koi bhi bimari, test result ya diagnosis explain karo – easy language me.
4. Agar koi concern ya serious finding ho, to usko highlight karo.
5. Common questions bhi anticipate karo aur unka answer do.
6. Agar kuch technical ya medical terms hain, unka meaning bhi batao.

Apna jawab clear headings aur bullet points ke sath do. Short aur simple raho, jise aam aadmi bhi samajh sake.
"""

# MAIN UI
st.title("🏥 ScanBuddy – Smart Medical Report Tool")
st.write("Upload a medical image or PDF report for professional analysis")

# ==== IF AGENT CONFIGURED, PROCEED ====
if medical_agent:
    # File uploader section
    col1, col2 = st.columns([5, 1])
    
    with col1:
        uploaded_file = st.file_uploader(
            "Upload Medical Image or PDF",
            type=["jpg", "jpeg", "png", "dicom", "pdf"],
            help="Supported formats: JPG, JPEG, PNG, DICOM, PDF"
        )
    
    with col1:
        if uploaded_file is not None:
            analyze_button = st.button("🔍 Analyze File", type="primary", use_container_width=True)
            
            # Check if we need to update analyzed_file in session_state
            if st.session_state.analyzed_file != uploaded_file.name:
                # This means a new file was uploaded
                st.session_state.analysis_result = None
                st.session_state.chat_history = []
    
    # Display uploaded content
    if uploaded_file is not None:
        resized_image = None
        extracted_text = ""
        
        # Create tabs for better organization
        tab1, tab2, tab3 = st.tabs(["Uploaded File", "Analysis Results", "Ask Questions"])
        
        with tab1:
            if uploaded_file.type in ["image/jpeg", "image/png", "image/gif", "image/bmp", "image/tiff"]:
                image = PILImage.open(uploaded_file)
                width, height = image.size
                aspect_ratio = width / height
                new_width = 500
                new_height = int(new_width / aspect_ratio)
                resized_image = image.resize((new_width, new_height))
                st.image(resized_image, caption="Uploaded Medical Image", use_container_width=True)
                
            elif uploaded_file.type == "application/pdf":
                pdf_reader = PyPDF2.PdfReader(uploaded_file)
                for page in pdf_reader.pages:
                    extracted_text += page.extract_text() or ""
                st.write("Uploaded PDF Content:")
                st.write(extracted_text)

        # Process analyze button click or use existing analysis
        if analyze_button:
            with st.spinner("🔄 Analyzing... Please wait."):
                try:
                    if uploaded_file.type == "application/pdf":
                        response = medical_agent.run(f"{pdf_query}\n\n{extracted_text}")
                    else:
                        image_bytes = BytesIO()
                        resized_image.save(image_bytes, format="PNG")
                        image_bytes.seek(0)

                        # If AgnoImage supports in-memory file:
                        agno_image = AgnoImage(content=image_bytes.read())
                        response = medical_agent.run(query, images=[agno_image])
                    # Save result in session state so it persists
                    st.session_state.analysis_result = response.content
                    st.session_state.analyzed_file = uploaded_file.name
                    st.session_state.chat_history = []  # Clear chat history when new analysis is done
                    
                    # Auto-switch to the Analysis Results tab
                    st.rerun()
                    
                except Exception as e:
                    st.error(f"Analysis error: {e}")
        
        # Display analysis results (tab 2)
        with tab2:
            if st.session_state.analysis_result:
                st.markdown("### 📋 Analysis Results")
                st.markdown("---")
                st.markdown(st.session_state.analysis_result)
                st.markdown("---")
                st.caption("Note: This analysis is generated by AI and should be reviewed by a qualified healthcare professional.")
                st.download_button("Download Analysis", st.session_state.analysis_result, file_name="analysis.txt", mime="text/plain")
            else:
                st.info("👆 Please click 'Analyze File' button to generate analysis")
        
        # Chat interface (tab 3)
        with tab3:
            if st.session_state.analysis_result:
                st.markdown("## 💬 Ask Questions About the Report")
                
                # Display chat history
                for role, msg in st.session_state.chat_history:
                    with st.chat_message(role):
                        st.markdown(msg)
                
                # Chat input
                user_question = st.chat_input("Ask anything about the uploaded report...")
                if user_question:
                    # Add user message to chat history
                    st.session_state.chat_history.append(("user", user_question))
                    
                    # Generate AI response
                    chat_prompt = f"""This is the medical report analysis:\n\n{st.session_state.analysis_result}\n\nThe user asked:\n{user_question}\n\nPlease answer clearly and helpfully based on the above analysis."""
                    with st.spinner("Thinking..."):
                        reply = medical_agent.run(chat_prompt)
                    
                    # Add AI response to chat history
                    st.session_state.chat_history.append(("ai", reply.content))
                    
                    # Force refresh to show the new messages
                    st.rerun()
                
                # Clear chat button
                if st.session_state.chat_history:
                    if st.button("🗑️ Clear Chat"):
                        st.session_state.chat_history = []
                        st.rerun()
            else:
                st.info("Please analyze the file first before asking questions")
    else:
        st.info("👆 Please upload a medical file to begin analysis")
else:
    st.warning("Please configure your API key to start analysis.")