import axios from "axios";
import { memo, VFC } from "react"
import { useCookies } from "react-cookie";
import { useForm } from "react-hook-form";
import { useHistory } from "react-router-dom";


export const Login: VFC = memo(() => {
    const apiURL = 'http://localhost:8000/api/'
    const history = useHistory();

    const [cookies, setCookie] = useCookies();
    const { register, handleSubmit, formState: { errors } } = useForm();
    
    const getJwt = async (data) =>{
        console.log(data);
        await axios.post(`${apiURL}auth/jwt/create/`,
          {
            username: data.username,
            password: data.password,
          },
        )
        .then(function (response) {
          console.log(response.data.access)
          setCookie('accesstoken', response.data.access, { path: '/' });
          setCookie('refreshtoken', response.data.refresh, { path: '/' });
          history.push('/');
        })
        .catch(err => {
            console.log("miss");
            alert("ユーザー名かパスワードが違います");
        });
      };

    return (
        <div>login</div>
    )
});
