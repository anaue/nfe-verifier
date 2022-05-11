from lxml import etree
from base64 import b64decode
from signxml import XMLVerifier
from signxml.exceptions import InvalidSignature, InvalidDigest, InvalidInput, InvalidCertificate

def verify_xml(fileContent):
    parser = etree.XMLParser()
    tree = etree.XML(fileContent, parser)

    bodyStr = ""
    certStr = ""

    body = tree.findall(".//{*}NFe")
    if not len(body):
        return "Could not read file content: NFe not defined."

    cert = tree.findall(".//{*}X509Certificate")
    if not len(cert):
        return "Could not read file content: X509Certificate not defined."

    try:
        bodyStr = etree.tostring(body[0])
        certStr = cert[0].text

        # it should raise exception if verification fails
        verifyResult = XMLVerifier().verify(bodyStr, x509_cert=certStr)

        return True
    except InvalidDigest as error:
        print(error)
        return "Invalid Digest " + str(error)
    except InvalidSignature as error:
        print(error)
        return "Invalid Signature " + str(error)
    except InvalidInput as error:
        print(error)
        return "Invalid Input " + str(error)
    except InvalidCertificate as error:
        print(error)
        return "Invalid Certificate " + str(error)
    except:
        print(len(parser.error_log))
        if len(parser.error_log):
            error = parser.error_log[0]
            print(error.message)
            return error.message
        return False