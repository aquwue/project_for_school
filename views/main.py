from flask import Flask, request, render_template
from flask_restx import abort, Namespace, Resource


main_ns = Namespace("main")


@main_ns.route('/')
class MainView(Resource):

    def get(self):
        # list_1 = read_json("data/data.json")
        # number = len_list("data/data.json")
        # list_2 = read_json("data/comments.json")

        return render_template('main.html')#, list_1=list_1, number=number, list_2=list_2)