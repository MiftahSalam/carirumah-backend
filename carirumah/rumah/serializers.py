from rest_framework import serializers
from rest_framework.validators import ValidationError

from .models import (
    Rumah, 
    ImageLink, 
    Source,
    Developer,
    Agent, 
)

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ['name']

class ImageLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageLink
        fields = ['url']
    
    def create(self,validated_data):
        print("ImageLinkSerializer create. data:",validated_data)
        return ImageLink.objects.create(**validated_data)
        # exit()
    
    def validate_property_name(self,value):
        print("ImageLinkSerializer validate_property_name. value:",value)
        return value

class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = ['name','contact']        
    
    def create(self,validated_data):
        print("DeveloperSerializer create:",validated_data)
        developer = None
        try:
            print("DeveloperSerializer create. Search for existing Developer")
            developer = Developer.objects.get(name=validated_data['name'])
            print("DeveloperSerializer create. Developer already exist")
        except Developer.DoesNotExist:
            print("DeveloperSerializer create name:",validated_data['name'])
            developer = Developer.objects.create(**validated_data)
        
        return developer
    
    def validate_name(self,value):
        print("DeveloperSerializer validate_name:",value)
        return value

    def validate_contact(self,value):
        print("DeveloperSerializer validate_contact:",value)
        return value

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['name','contact']

    def create(self,validated_data):
        print("AgentSerializer create:",validated_data)
        agent = None
        try:
            print("AgentSerializer create. Search for existing Agent")
            agent = Agent.objects.get(name=validated_data['name'])
            print("AgentSerializer create. Agent already exist")
        except Agent.DoesNotExist:
            print("AgentSerializer create name:",validated_data['name'])
            agent = Agent.objects.create(**validated_data)
        
        return agent
    
    def validate_name(self,value):
        print("AgentSerializer validate_name:",value)
        return value

    def validate_contact(self,value):
        print("DeveloperSerializer validate_contact:",value)
        return value

class BriefRumahSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    property_name = serializers.CharField(read_only=True)
    address = serializers.CharField(read_only=True)
    property_type = serializers.CharField(read_only=True)
    LB = serializers.CharField(read_only=True)
    LT = serializers.CharField(read_only=True)
    image_link = ImageLinkSerializer(source='imagelink_set', many=True)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if len(ret["image_link"]) > 0:
            ret["image_link"] = ret["image_link"][0]
        return ret

class RumahSerializer(serializers.ModelSerializer):
    images = ImageLinkSerializer(source='imagelink_set', many=True)
    agent = AgentSerializer(many=True)

    class Meta:
        model = Rumah
        fields = [
            'id',
            'source',
            'property_name',
            'address',
            'price',
            'LT',
            'LB',
            'property_type',
            'description',
            'release_date',
            'publish_date',
            'developer',
            'agent',
            'facility',
            'status',
            'certificate',
            'images',
        ]

    # def to_internal_value(self,*args,**kwargs):
    #     try:
    #         return super().to_internal_value(*args,**kwargs)
    #     except ValidationError:
    #         return self.validate(self.initial_data)

    def create(self,validated_data):
        print("RumahSerializer create. data:",validated_data)
        rumah = None

        agent_instance = None
        agent_data = None
        try: 
            agent_data = validated_data['agent']
        except:
            print("agent not available")

        try:
            agent_instance = Agent.objects.get(name=agent_data[0]['name'])
        except:
            print("cannot get agent")

        try:
            print("RumahSerializer create. check for existing property_name")
            rumah = Rumah.objects.get(property_name=validated_data['property_name'])
            print("RumahSerializer create. property_name already exist")
            print("RumahSerializer create. check for update agent")
            if agent_instance != None:
                print("RumahSerializer create. add agent:",agent_data[0])
                rumah.agent.add(agent_instance)                
            else:
                print("RumahSerializer create. agent already exist")

        except Rumah.DoesNotExist:
            print("RumahSerializer create property_name:",validated_data['property_name'])
            images_link = validated_data['imagelink_set']

            try:
                del validated_data['imagelink_set']
            except:
                print('RumahSerializer create. Failed to delete imagelink_set')
            
            try:
                del validated_data['agent']
                agent_serializer = AgentSerializer(data=agent_data[0])
                if agent_serializer.is_valid(raise_exception=True):
                    print("agent_serializer valid")
                    agent_serializer.save()
                    agent_instance = Agent.objects.get(name=agent_serializer.data['name'])
            except:
                print('RumahSerializer create. Failed to delete agent')

            rumah = Rumah.objects.create(**validated_data)
            if agent_instance != None: rumah.agent.add(agent_instance)

            for i_link in images_link:
                i_data = {'url':i_link['url'],'property_name': rumah} 
                # print("RumahSerializer creating images link...")
                image_link = ImageLink.objects.create(**i_data)

        return rumah



