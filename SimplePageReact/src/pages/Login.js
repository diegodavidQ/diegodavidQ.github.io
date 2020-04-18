import React from 'react';

import Title from '../components/Title';
import Container from '../components/Container';

import TextField from 'material-ui/TextField';
import RaisedButton from 'material-ui/RaisedButton';
import {login, signUp} from '../requests/auth';

import {
    BrowserRouter as ReactRouter,
    Link,
    Route
} from 'react-router-dom';

export default class Login extends React.Component {
    
    constructor(props){
        super(props);

        this.resquestAuth = this.resquestAuth.bind(this);
        this.createAccount = this.createAccount.bind(this);
    }

    resquestAuth(){
        const credentials = {
            email: this.refs.emailField.getValue(),
            password: this.refs.passwordField.getValue()
        }

        login(credentials).then(console.log).catch(console.log);
    }
    
    createAccount(){
        const credentials = {
            email: this.refs.emailField.getValue(),
            password: this.refs.passwordField.getValue()
        }

        signUp(credentials).then(console.log).catch(console.log);

    }

    render() {
        return (
                <div className="row middle-xs">
                    <div className="col-xs-12 col-sm-6">
                        <Container>
                            <div style={{ 'textAlign': 'left' }}>
                                <Title />
                                <TextField
                                    floatingLabelText="Correo electrónico"
                                    type="email"
                                    className="textfield"
                                    ref="emailField"
                                />
                                <TextField
                                    floatingLabelText="Contraseña"
                                    type="password"
                                    className="textfield"
                                    ref="passwordField"
                                />
                                <div className="Login-actions">
                                    <Route path="/login" exact render={() => {
                                        return (
                                            <div>
                                                <Link to="/signup" style={{ marginRight: "1em" }}>Crear nueva cuenta</Link>
                                                <RaisedButton onClick={this.resquestAuth} label="Ingresar" secondary={true} />
                                            </div>
                                        );
                                    }}></Route>

                                    <Route path="/signup" exact render={() => {
                                        return (
                                            <div>
                                                <Link to="/login" style={{ marginRight: "1em" }}>Ya tengo cuenta</Link>
                                                <RaisedButton onClick={this.createAccount} label="Crear cuenta" secondary={true} />
                                            </div>
                                        );
                                    }}></Route>
                                    <Link to="/" style={{ marginRight: "1em" }}>Inicio</Link>
                                </div>
                            </div>
                        </Container>
                    </div>
                    <div className="col-xs-12 col-sm-6">
                        <div>
                            <Route path="/login" exact render={() =>
                                <div className="Login-background" style={{
                                    'backgroundImage':
                                        "url(" + process.env.PUBLIC_URL + "/images/Login-background.jpg" + ")"
                                }}></div>
                            }></Route>

                            <Route path="/signup" exact render={() => 
                                <div className="Login-background" style={{
                                    'backgroundImage':
                                        "url(" + process.env.PUBLIC_URL + "/images/compartir.jpg" + ")"
                                }}></div>
                            }></Route>

                        </div>
                    </div>
                </div>
        )
    }
} 