Vim�UnDo� }�CƓO�s�V�|������H�n|��X�9]   *       "          E       E   E   E    ]$pi    _�                             ����                                                                                                                                                                                                                                                                                                                                       
           V        ]$L�     �                    app = Flask(__name__)   (    app.config['SECRET_KEY'] = 'secret!'    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ]$L�     �             �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       ]$L�    �                   app = Flask(__name__)   (    app.config['SECRET_KEY'] = 'secret!'5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ]$M�     �                    @app.route('/')       def index():   ,        return render_template('index.html')           @socketio.on('my event')       def test_message(message):   0        emit('my response', {'data': 'got it!'})5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ]$M�     �             �      	       5�_�                    	        ����                                                                                                                                                                                                                                                                                                                            	                    V       ]$M�    �                   @app.route('/')       def index():   ,        return render_template('index.html')           @socketio.on('my event')       def test_message(message):   0        emit('my response', {'data': 'got it!'})5�_�                            ����                                                                                                                                                                                                                                                                                                                            	                    V       ]$M�     �                 5�_�      
                      ����                                                                                                                                                                                                                                                                                                                            	                    V       ]$M�    �                 5�_�         	       
           ����                                                                                                                                                                                                                                                                                                                                                             ]$O�     �                (from flask import Flask, render_template    �                �             5�_�   
                         ����                                                                                                                                                                                                                                                                                                                                                             ]$O�     �                (from flask import Flask, render_template5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]$O�     �                �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]$O�     �                  5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]$O�    �                m gevent import monkey5�_�                    
        ����                                                                                                                                                                                                                                                                                                                                       
           V        ]$Q�     �   	   
              @app.route('/')   def index():   (    return render_template('index.html')       @socketio.on('my event')   def test_message(message):   ,    emit('my response', {'data': 'got it!'})5�_�                            ����                                                                                                                                                                                                                                                                                                                            
           
           V        ]$Q�     �             �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ]$Q�     �               @app.route('/')   def index():   (    return render_template('index.html')       @socketio.on('my event')   def test_message(message):   ,    emit('my response', {'data': 'got it!'})5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        ]$Q�    �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ]$Q�     �                    @app.route('/')       def index():   ,        return render_template('index.html')5�_�                    
        ����                                                                                                                                                                                                                                                                                                                                                  V        ]$Q�     �   
          �   
          5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       ]$Q�     �   
                @app.route('/')       def index():   ,        return render_template('index.html')5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       ]$Q�     �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       ]$Q�     �                 5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       ]$Q�    �                dd5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       ]$R7     �                 �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       ]$R9     �         "       5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       ]$R:     �         #       5�_�                      !    ����                                                                                                                                                                                                                                                                                                                                                V       ]$S�   	 �         $      (    return render_template('index.html')5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]$T#     �         %       �         $    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       ]$T)     �         *      0        print('received my event: ' + str(json))   D        socketio.emit('my response', json, callback=messageReceived)5�_�      !                       ����                                                                                                                                                                                                                                                                                                                                                V       ]$T0     �                    @socketio.on('my event')       def test_message(message):   0        emit('my response', {'data': 'got it!'})5�_�       "           !           ����                                                                                                                                                                                                                                                                                                                                                V       ]$T1     �                 5�_�   !   #           "           ����                                                                                                                                                                                                                                                                                                                                                V       ]$T2   
 �                 5�_�   "   $           #   	       ����                                                                                                                                                                                                                                                                                                                                                V       ]$T�     �   	      %    �   	   
   %    5�_�   #   %           $   	        ����                                                                                                                                                                                                                                                                                                                                                V       ]$T�     �      
   &      (socketio = SocketIO(async_handlers=True)5�_�   $   &           %   
   '    ����                                                                                                                                                                                                                                                                                                                                                V       ]$T�     �   	      &      (socketio = SocketIO(async_handlers=True)5�_�   %   '           &           ����                                                                                                                                                                                                                                                                                                                                                V       ]$T�     �          &      from gevent import monkey5�_�   &   (           '           ����                                                                                                                                                                                                                                                                                                                                                V       ]$T�    �         &      monkey.patch_all()5�_�   '   )           (           ����                                                                                                                                                                                                                                                                                                                                                V       ]$T�     �          &      #from gevent import monkey5�_�   (   *           )           ����                                                                                                                                                                                                                                                                                                                                                V       ]$T�     �         &      #monkey.patch_all()5�_�   )   +           *   	        ����                                                                                                                                                                                                                                                                                                                                                V       ]$T�     �      
   &      )#socketio = SocketIO(async_handlers=True)5�_�   *   ,           +   
        ����                                                                                                                                                                                                                                                                                                                                                V       ]$T�    �   	   
          socketio = SocketIO()5�_�   +   -           ,          ����                                                                                                                                                                                                                                                                                                                                                V       ]$U�     �         %    �         %    5�_�   ,   .           -          ����                                                                                                                                                                                                                                                                                                                                                V       ]$U�     �         &      8    socketio.init_app(app) #, async_mode="gevent_uwsgi")5�_�   -   /           .          ����                                                                                                                                                                                                                                                                                                                                                V       ]$U�     �         &      8    socketio.init_app(app) #, async_mode="gevent_uwsgi")5�_�   .   0           /          ����                                                                                                                                                                                                                                                                                                                                                V       ]$U�    �         &      9    #socketio.init_app(app) #, async_mode="gevent_uwsgi")5�_�   /   1           0      -    ����                                                                                                                                                                                                                                                                                                                                                V       ]$U�     �         &      5    socketio.init_app(app, async_mode="gevent_uwsgi")5�_�   0   2           1      -    ����                                                                                                                                                                                                                                                                                                                                                V       ]$U�     �         &      4    socketio.init_app(app, async_mode="geventuwsgi")5�_�   1   3           2      -    ����                                                                                                                                                                                                                                                                                                                                                V       ]$U�     �         &      3    socketio.init_app(app, async_mode="geventwsgi")5�_�   2   4           3      -    ����                                                                                                                                                                                                                                                                                                                                                V       ]$U�     �         &      2    socketio.init_app(app, async_mode="geventsgi")5�_�   3   5           4      -    ����                                                                                                                                                                                                                                                                                                                                                V       ]$U�     �         &      1    socketio.init_app(app, async_mode="geventgi")5�_�   4   6           5      -    ����                                                                                                                                                                                                                                                                                                                                                V       ]$U�    �         &      0    socketio.init_app(app, async_mode="geventi")5�_�   5   9           6      -    ����                                                                                                                                                                                                                                                                                                                                                V       ]$j    �         &      /    socketio.init_app(app, async_mode="gevent")5�_�   6   :   7       9      4    ����                                                                                                                                                                                                                                                                                                                                                V       ]$l�     �         &      5    socketio.init_app(app, async_mode="gevent_uwsgi")5�_�   9   ;           :      8    ����                                                                                                                                                                                                                                                                                                                                                V       ]$l�     �         &      L    socketio.init_app(app, async_mode="gevent_uwsgi", , async_handlers=True)5�_�   :   <           ;   	   '    ����                                                                                                                                                                                                                                                                                                                                                V       ]$l�    �      
   &      (socketio = SocketIO(async_handlers=True)5�_�   ;   =           <      6    ����                                                                                                                                                                                                                                                                                                                                                V       ]$m�    �         &      J    socketio.init_app(app, async_mode="gevent_uwsgi", async_handlers=True)5�_�   <   >           =           ����                                                                                                                                                                                                                                                                                                                                                V       ]$n$     �         &      app = Flask(__name__)   $app.config['SECRET_KEY'] = 'secret!'       socketio = SocketIO()       @app.route('/')   def index():   *    return render_template('session.html')           @socketio.on('my event')   :def handle_my_custom_event(json, methods=['GET', 'POST']):   ,    print('received my event: ' + str(json))   @    socketio.emit('my response', json, callback=messageReceived)           -def messageReceived(methods=['GET', 'POST']):   $    print('message was received!!!')5�_�   =   ?           >           ����                                                                                                                                                                                                                                                                                                                                                V       ]$n'     �                def create_app():5�_�   >   @           ?          ����                                                                                                                                                                                                                                                                                                                                                V       ]$n*     �         %    �         %    5�_�   ?   A           @           ����                                                                                                                                                                                                                                                                                                                                                V       ]$n+    �         '       �         &    5�_�   @   B           A           ����                                                                                                                                                                                                                                                                                                                            	                    V       ]$n=     �                    socketio = SocketIO()5�_�   A   C           B           ����                                                                                                                                                                                                                                                                                                                            	                    V       ]$n@     �         '    �         '    5�_�   B   D           C          ����                                                                                                                                                                                                                                                                                                                            
                    V       ]$nA    �         (          socketio = SocketIO()5�_�   C   E           D   !        ����                                                                                                                                                                                                                                                                                                                            
                    V       ]$pf     �   !   $   )       �   !   #   (    5�_�   D               E   "        ����                                                                                                                                                                                                                                                                                                                            
                    V       ]$ph    �   !   #   *       5�_�   6   8       9   7          ����                                                                                                                                                                                                                                                                                                                                                V       ]$lX     �         &          socketio.init_app(app)5�_�   7               8          ����                                                                                                                                                                                                                                                                                                                                                V       ]$lY    �         &      6    #socketio.init_app(app, async_mode="gevent_uwsgi")5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       ]$Rj     �         $          def test_message(message):�         $      8    @socketio.on('my event    def test_message(message):5�_�              
   	           ����                                                                                                                                                                                                                                                                                                                                                             ]$O�     �                �               from gevent import monkey   monkey.patch_all()5��