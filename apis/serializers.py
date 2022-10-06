import xml.etree.ElementTree as ET

from rest_framework import serializers
from .models import apiModel

class apiSerializer(serializers.ModelSerializer):
    ref_list = serializers.SerializerMethodField()
    def get_ref_list(self,apiModel):
        tree = ET.parse(apiModel.xml_file)
        root = tree.getroot()
        d ={}
        li = []

        for ele in root.findall(".//ref-list/"):
            # ele -> 299 ->d contains 299 ref

            for child in ele:
                dic = {}
                # child -> 1 -> dic contains 1 ref
                if child.tag == "label":
                    label = child.text
                    d[label] = {}
                    prev = ele
                else:
                    dic[prev.tag] = prev.attrib
                    dic[child.tag] = child.attrib
                    dic["string-name"] = []
                    for child2 in child.findall('.//'):
                        # all tags under mixed-citation
                        if child2.tag == "person-group":
                            dic[child2.tag] = child2.attrib
                            continue
                        if child2.tag == "string-name":
                            given = {}
                            for child3 in child2:

                                # sur = {}
                                if child3.tag == "given-names":
                                    given[child3.tag] = child3.text
                                    # dic["string-name"].append(given)
                                    continue
                                if child3.tag == "surname":
                                    given[child3.tag] = child3.text
                                    dic["string-name"].append(given)
                                    continue

                        else:
                            if child2.tag == "given-names" or child2.tag == "surname":
                                continue


                            if child2.tag not in dic:
                                dic[child2.tag] = child2.text
                    d[label] = dic
                    li.append(d[label])
        return li

    class Meta:
        model = apiModel
        fields = ('xml_file','ref_list')
        