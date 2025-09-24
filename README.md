# 📄 Write of Access
**Handwritten Court Form OCR with AWS Textract**  
_Prototype to test extraction of typed and handwritten data from public court forms using Textract._

---

## ⚙️ Overview

**Write of Access** is a prototype project designed to evaluate the capabilities and limitations of AWS Textract for extracting typed and handwritten data from scanned court forms. It is particularly focused on structured forms like the *Copy Request Form* used in California trial courts.

This repo contains:
- Textract-based OCR scripts
- A sample scanned public form
- Simulated OCR output files
- Validation templates and documentation
- Placeholder test architecture

---

## 📁 Folder Structure

```
Write_of_Access/
├── docs/
│   └── validation_log_template.md
├── input/
│   └── copyrequest (5).pdf
├── output/
│   └── sample_form_1_pg1_processed.txt
├── scripts/
│   ├── convert_and_preprocess.py
│   ├── textract_call.py
│   ├── textract_document_ocr.py
│   └── textract_test.py
└── README.md
```

---

## 📷 Visual Walkthrough

| Input PDF | Converted PNG | Processed Output |
|-----------|----------------|------------------|
| `copyrequest (5).pdf` | `input/png/copyrequest_pg1.png` | `output/sample_form_1_pg1_processed.txt` |

*Note: Due to privacy restrictions, sample PNGs and outputs have been simulated for demo purposes.*

---

## 🔍 Key Limitations

- Textract struggles with checkboxes and overlapping handwriting.
- Signature and date fields can be partially recognized but not consistently.
- Manual review is required before trustable automation.

---

## 🧱 Architecture Diagram

```
+-----------------------+
|   Scanned PDF Input   |
+----------+------------+
           |
           v
+-----------------------+
| Convert to PNG Images |
+----------+------------+
           |
           v
+-------------------------+
|   AWS Textract (OCR)    |
+----------+--------------+
           |
           v
+-------------------------+
|  Parsed Text Output     |
+-------------------------+
           |
           v
+-------------------------+
|   Manual Validation     |
+-------------------------+
```

---

## 🚀 Usage Instructions

1. Place scanned PDF(s) in the `input/` folder.
2. Run Textract with `scripts/textract_call.py` or `scripts/textract_test.py`.
3. Review generated `.txt` output in the `output/` folder.
4. Complete a validation log using `docs/validation_log_template.md`.

---

## 🧪 Placeholder Scripts
These can be extended as needed:
- `run_textract_ocr.py`: Entry point script to call Textract API.
- `convert_and_preprocess.py`: Converts PDFs to PNGs, applies binarization/rotation.
- `textract_test_runner.py`: Local/offline testing without live AWS calls.

---

## 📚 License
This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and build upon it.

---

## 🙋‍♀️ About This Project

This is a civic-tech prototype by a public servant exploring real-world AI integration in courts. No sensitive data is used. Sample forms are public, and outputs are simulated.

## 🤝 Acknowledgements

This project was prototyped using OpenAI’s ChatGPT, which served as the sixth person off the bench — helping with Python scripting, AWS Textract integration, architecture planning, and documentation support. All judgment calls, design decisions, and final outputs were authored and validated by the project owner.
