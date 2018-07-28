import inspect
import os
import os.path
import subprocess
import sys
from shutil import copyfile
from tempfile import gettempdir

# check node is installed first!
# npm install in reveal_js_dir

# para shadertoy offline
# C:\work>mkdir sto & cd sto
# git clone https://github.com/tdhooper/offline-shadertoy src & cd src
# npm install budo -g
# npm install glslify
# C:\work\sto\src>npm start
# edit c:\work\sto\src\projects\impossible-channel\shader.glsl
# use play() and pause() in FF JavaScript console

# present_work_dir = gettempdir()
present_work_dir = os.environ['USERPROFILE']
present_work_dir = os.path.join(present_work_dir, "eci")
reveal_js_dir = os.path.join(present_work_dir, "reveal.js")
mathjax_dir = os.path.join(reveal_js_dir, "lib", "MathJax")
utils_dir = os.path.dirname(os.path.abspath(__file__))
repo_root_dir = os.path.normpath(os.path.join(utils_dir, ".."))

def replace_text_in_file(file_name, start_marker, end_marker, new_text):
    with open(file_name, 'r') as f:
        content = f.read()    
    start_index = content.index(start_marker)
    end_index = content.index(end_marker)
    new_content = content[:start_index] + start_marker + new_text + content[end_index:]
    with open(file_name, 'w') as f:
        f.write(new_content)    
        
def setup():
    print("setting up on " + present_work_dir)
    if not os.path.exists(present_work_dir):
        os.mkdir(present_work_dir)
    if not os.path.exists(reveal_js_dir):
        print("cloning reveal.js")
        subprocess.call(["git", "clone", "https://github.com/hakimel/reveal.js.git", reveal_js_dir])
    print("setting up reveal on " + reveal_js_dir)
    if not os.path.exists(os.path.join(reveal_js_dir, "package-lock.json")):
        print("installing npm pacakges")
        subprocess.call(["cmd", "/C", "npm", "install"], cwd=reveal_js_dir)
    if not os.path.exists(mathjax_dir):
        print("cloning MathJax.js")
        subprocess.call(["git", "clone", "https://github.com/mathjax/MathJax/", mathjax_dir])
    print("copying content files")
    files_source_dir = repo_root_dir
    mon_files_to_copy = [
        # lunes
        "intro",
        "arquitecture-soft",
        "libs",
        "langs",
        "pixels",
    ]
    tue_files_to_copy = [
        # martes
        "intro2",
        "tess",
        "percepcion",
        "geometria",
        "transform",
        "gcn",
        "programables",
        "fijas",
        "caches",
        "performance-intro",
    ]
    wed_files_to_copy = [
        # miercoles
        "intro2",
        "representaciones",
        "animacion",
    ]
    thu_files_to_copy = [
        # jueves
        "ml",
        "frameworks",
        "eval",
        "modelos-prog",
        "color"
        ]
    fri_files_to_copy = [
        # viernes
        "vcpkg",
        "performance",
        "meshes",
        "camaras",
        "mobile",
        "escenas",
        "tp"
        ]
    files_to_copy = fri_files_to_copy
    # files_to_copy = [ "ml" ] # usen esto para ver uno en particular
    sections_text = ""
    for f in files_to_copy:
        sections_text += "<section data-markdown='lib/" + f + ".md' " + \
          r"data-separator='^\r?\n\r?\n\r?\n' " + \
          r"data-separator-notes='Notas:' " + \
          "data-charset='utf-8'></section>\r\n"
        copyfile(os.path.join(files_source_dir, f + ".md"), os.path.join(reveal_js_dir, "lib", f + ".md"))
    print("setting up index with copied content ...")
    copyfile(os.path.join(utils_dir, "reveal-index.html"), os.path.join(reveal_js_dir, "index.html"))
    replace_text_in_file(os.path.join(reveal_js_dir, "index.html"), "<!--generated starts-->", "<!--generated ends-->", sections_text)
    print("copying external and asset files to images ...")
    subprocess.call(["robocopy", os.path.join(repo_root_dir, "assets"), os.path.join(reveal_js_dir, "images"), "/NFL", "/NJH"])
    subprocess.call(["robocopy", os.path.join(repo_root_dir, "external"), os.path.join(reveal_js_dir, "images"), "/NFL", "/NJH"])

def run():
    subprocess.call(["start", "cmd", "/K", "node", "plugin/notes-server"], cwd=reveal_js_dir, shell=True)
    
if __name__ == "__main__":
    setup()
    run()

