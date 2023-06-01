import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Response;
import retrofit2.Retrofit;

import java.io.IOException;

public class Main {

    public static final int SOME_STRANGE_NUMBER = 1184112;

    public static void main(String[] args) throws IOException {
        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("https://innovationcampus.ru/lms/")
                .build();

        GitHubService service = retrofit.create(GitHubService.class);

        Call<ResponseBody> numberCall = service.getNumber();

        Response<ResponseBody> response = numberCall.execute();
        int divider = Integer.parseInt(response.body().string());
        int result = SOME_STRANGE_NUMBER / divider;
        System.out.println(result);
        response.body().close();
    }
}

