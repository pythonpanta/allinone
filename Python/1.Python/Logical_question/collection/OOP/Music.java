package OOP;

public class Music implements MusicPlayer{
    @Override
    public void start() {
        System.out.println("Music Playing");
    }

    @Override
    public void stop() {
        System.out.println("Peace");
    }
}
