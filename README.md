### Workshop: Pentaho Data Catalog 10.1

This workshop introduces the Pentaho Data Catalog and its capabilities to manage both structured and unstructured data efficiently. Through a combination of automated processes and machine learning, the course will guide you through the essential functions of data ingestion, profiling, and curation. You will learn how to connect to various data sources, understand the importance of a business glossary, enforce metadata rules, and gain insights into the components of the Pentaho+ Data Catalog.
By the end of the workshop, participants will have a comprehensive understanding of:

- Key Concepts & Terminology: Familiarize yourself with the foundational terminology and concepts used within the Pentaho Data Catalog environment.
- Connecting to Various Data Sources: Learn how to establish connections to a wide range of data sources to enable data ingestion.
- Ingesting & Profiling Data: Discover the methods used for data ingestion and how profiling assists in understanding your data's structure and quality.
- Business Glossary & Terms: Understand the significance of maintaining a business glossary and how it aids in aligning data with business terminology.
- Rules: Explore how metadata rules are applied to data within the Pentaho Data Catalog to ensure consistency and relevance.
- Pentaho Data Catalog Components: Get an insight into the various components that make up the Pentaho Data Catalog and how they interact to provide a comprehensive data management solution.

#### Notes on PDC/PDO

Resolved using SKytap DNS
Domain: pentaho.example (10.0.0.254)

* Ensure you add the HCP Certificate to the PDC server
* HCP Certificate located: Tenant -> Replication

keytool -trustcacerts -keystore "%JAVA_HOME%jre\lib\security\cacerts" -storepass changeit -importcert -alias HCProot -file ~/Downloads/certificate.crt
Owner: CN=*.hcp1.pentaho.plus, OU=HCP, O=Hitachi, L=Waltham, ST=Massachusetts, C=US
Issuer: CN=*.hcp1.pentaho.plus, OU=HCP, O=Hitachi, L=Waltham, ST=Massachusetts, C=US
Serial number: 54efb8520990a54e6768d4e6f2e515a53accb7b
Valid from: Thu May 16 11:42:23 BST 2024 until: Wed May 16 11:42:23 BST 2029
Certificate fingerprints:
	 SHA1: 21:19:47:37:16:63:E9:FA:E8:EF:C1:95:01:B5:CD:EE:02:1C:55:21
	 SHA256: 48:9C:8B:EC:FB:5B:A2:31:49:13:F3:33:B0:B9:3C:E6:C3:C7:F0:A1:A6:D8:99:A3:22:01:36:C1:9F:FB:81:61
Signature algorithm name: SHA256withRSA
Subject Public Key Algorithm: 2048-bit RSA key
Version: 3

Extensions: 

#1: ObjectId: 2.5.29.35 Criticality=false
AuthorityKeyIdentifier [
KeyIdentifier [
0000: 4A 88 08 A7 E5 2C 02 F6   E7 F3 C4 7F 06 44 01 66  J....,.......D.f
0010: 17 76 5E 16                                        .v^.
]
]

#2: ObjectId: 2.5.29.19 Criticality=true
BasicConstraints:[
  CA:true
  PathLen: no limit
]

#3: ObjectId: 2.5.29.14 Criticality=false
SubjectKeyIdentifier [
KeyIdentifier [
0000: 4A 88 08 A7 E5 2C 02 F6   E7 F3 C4 7F 06 44 01 66  J....,.......D.f
0010: 17 76 5E 16                                        .v^.
]
]

Trust this certificate? [no]:  yes
Certificate was added to keystore



#### Notes on Windows Server 2022

Username: Administrator
Password: Welcome123!
DNS Domain: pentaho.plus
HCP Forwarding: *.hcp1.pentaho.plus

#### Notes on HCP 9.4.4

System Account
Username: admin
Password: Pentaho123!
Endpoint: https://PentahoTNT.hcp1.pentaho.plus

Tenant Accounts
PentahoTNT - administration account
Username: PentahoTNT
Password: Pentaho123!

s3user - data account
Username: s3user
Password123!
Namespace: Bucket1
