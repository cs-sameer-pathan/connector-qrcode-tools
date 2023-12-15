
<h2>About the connector</h2>

<p>QRCode Tools helps users working with QR and Bar codes</p>

<p>This document provides information about the QRCode Tools Connector, which facilitates automated interactions, with a QRCode Tools server using FortiSOAR&trade; playbooks. Add the QRCode Tools Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with QRCode Tools.</p>

<h3>Version information</h3>

<p>Connector Version: 1.0.0</p>

<p>Authored By: Fortinet CSE</p>

<p>Contributors: Naili Mahdi</p>

<p>Certified: No</p>

<h2>Installing the connector</h2>

<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>

<pre>yum install cyops-connector-qrcode-tools</pre>

<h2>Prerequisites to configuring the connector</h2>

<p>There are no prerequisites to configuring this connector.</p>

<h2>Minimum Permissions Required</h2>

<ul>
<li>Not applicable</li>
</ul>

<h2>Configuring the connector</h2>

<p>For the procedure to configure a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector">here</a></p>

<h3>Configuration parameters</h3>

<p>None.</p>

<h2>Actions supported by the connector</h2>

<p>The following automated operations can be included in playbooks and you can also use the annotations to access operations:</p>

<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Read QR/Bar Code</td><td>Read QR/Bar code(s) from an image file or attachment</td><td>read_qr_code <br/>Investigation</td></tr>
</tbody></table>

<h3>operation: Read QR/Bar Code</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>File IRI</td><td>IRI of the image file or attachment with the QR/Bar code(s) to read
</td></tr></tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>[
    {
        "text": "",
        "format": "",
        "content": "",
        "position": ""
    }
]</pre>

<h2>Included playbooks</h2>

<p>The <code>Sample - qrcode-tools - 1.0.0</code> playbook collection comes bundled with the QRCode Tools connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the <strong>Automation</strong> &gt; <strong>Playbooks</strong> section in FortiSOAR&trade; after importing the QRCode Tools connector.</p>

<ul>
<li>Read QR/Bar Code</li>
</ul>

<p><strong>Note</strong>: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.</p>
