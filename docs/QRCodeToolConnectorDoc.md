## About the connector
QRCode Tools helps users working with QR and Bar codes
<p>This document provides information about the QRCode Tools Connector, which facilitates automated interactions, with a QRCode Tools server using FortiSOAR&trade; playbooks. Add the QRCode Tools Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with QRCode Tools.</p>

#### Version information

Connector Version: 1.0.1

FortiSOAR&trade; Version Tested on: 7.5.0-4015

Authored By: Fortinet

Certified: Yes
## Release Notes for version 1.0.1
Following enhancements have been made to the QRCode Tools Connector in version 1.0.1:
<ul>
<li>Added support to specify name or path of the file in /tmp directory to read the QR(Bar) code.</li>
</ul>

## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p>
<p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-qrcode-tools</pre>

## Prerequisites to configuring the connector
There are no prerequisites to configuring this connector.

## Minimum Permissions Required
- Not applicable

## Actions supported by the connector
The following automated operations can be included in playbooks, and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Read QR/Bar Code</td><td>Read QR/Bar code(s) from an image file or attachment</td><td>read_qr_code <br/>Investigation</td></tr>
</tbody></table>

### operation: Read QR/Bar Code
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Input Type</td><td>Specify the type of input that you want to submit to read the QR code. The input type can be an IRI or a File Path.
<br><strong>If you choose 'IRI'</strong><ul><li>File IRI/Attachment IRI: Specify the IRI of the image file or attachment with the QR/Bar code(s) to read.</li></ul><strong>If you choose 'File Path'</strong><ul><li>File Path: Specify the name or path the file whose QR/Bar code(s) to read.</li></ul></td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>[
    {
        "text": "",
        "format": "",
        "content": "",
        "position": ""
    }
]</pre>

## Included playbooks
The `Sample - qrcode-tools - 1.0.1` playbook collection comes bundled with the QRCode Tools connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the QRCode Tools connector.

- Read QR/Bar Code

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.


## Troubleshooting

- When receiving below error 
   >libGL.so.1: cannot open shared object file: No sch file or directory

    <b>Resolution</b>: Install libGLU package using below command

        `yum install libGLU`
- When receiving below error
   > Unable to get page count. Is poppler installed and in PATH?

  <b>Resolution</b>: Install the development libraries for Poppler
   
        `yum install poppler-utils`

