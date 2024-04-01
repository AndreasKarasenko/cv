from rendercv.renderer import latex_to_pdf
import pathlib

path = pathlib.Path("./rendercv_output/Andreas_Karasenko_CV.tex")
latex_to_pdf(path)