import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.http.GET;

public interface GitHubService {
    @GET("getnumber/")
    Call<ResponseBody> getNumber();
}
