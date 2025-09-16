import streamlit as st
import subprocess
import os
import sys
from pathlib import Path

st.set_page_config(page_title="My Project Portfolio", layout="wide")
st.title("My Full-Stack Project Portfolio 🚀")
st.markdown("""
Welcome! Click **Run Project Locally** to fetch the LocalGlobalRunner and run the project.
""")

# Paths
REPO_ROOT = Path(__file__).parent
LGR_PATH = REPO_ROOT / "LocalGlobalRunner"

# GitHub URL for your LocalGlobalRunner repo
LGR_GITHUB = "https://github.com/ARUNAWRISHE/LocalGlobalRunner.git"

def install_runner():
    if not LGR_PATH.exists():
        st.info("Downloading LocalGlobalRunner from GitHub...")
        subprocess.run(f"git clone {LGR_GITHUB} {LGR_PATH}", shell=True, check=True)
    sys.path.insert(0, str(LGR_PATH))
    import generator
    generator.create(REPO_ROOT)
    generator.copy(REPO_ROOT)

if st.button("Run Project Locally"):
    try:
        install_runner()
        st.success("Project setup done! You can now run it with the launcher.")
    except Exception as e:
        st.error(f"Failed to run: {e}")

