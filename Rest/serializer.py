from rest_framework import serializers
from .models import Todo,TimingTodo
import re
from django.template.defaultfilters import slugify

class TodoSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()


    class Meta:
        model = Todo
        # fields = '__all__'
        fields = ['todo_title','slug','todo_description','is_done','uid']

        # for spacific validation

    
    def get_slug(self, obj):
         return slugify(obj.todo_title)
         


    def validate_todo_title(self, data):
            if data:
                todo_title = data
                regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
                
                if len(todo_title)<3:
                     raise serializers.ValidationError('todo_title mustbe morethan 3 character')

                if not regex.search(todo_title) == None:
                    # print("String is accepted")
                    raise serializers.ValidationError('todo_title cannot contains special characters')
            return data


    # def validate(self, validated_data):
    #         if validated_data.get('todo_title'):
    #             todo_title = validated_data['todo_title']
    #             regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
                
    #             if len(todo_title)<3:
    #                  raise serializers.ValidationError('todo_title mustbe morethan 3 character')

    #             if not regex.search(todo_title) == None:
    #                 # print("String is accepted")
    #                 raise serializers.ValidationError('todo_title cannot contains special characters')
    #         return validated_data

         
                # else:
                #     print("String is not accepted.")





class TimingTodoSerializer(serializers.ModelSerializer):
        todo = TodoSerializer()  # for giting the forign key data
        class Meta:
             model = TimingTodo
             exclude = ['created_at', 'updated_at']
            #  depth = 1    # for giting the forign key data


