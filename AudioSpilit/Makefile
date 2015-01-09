
# LIBS = -lavformat -lavcodec -lva -lXfixes -lXext -lX11 -lasound -lSDL -lx264 -lvpx -lvorbisenc -lvorbis -ltheoraenc -ltheoradec -logg -lopus -lmp3lame -lfreetype -lfdk-aac -lass -lz -lswresample -lswscale -lavutil -lm

# all: spilittool

# spilittool: spilittool.o
# 	$(CC) -Wall -g -o $^ $(LIBS)

# spilittool.o: spilittool.c
# 	$(CC) -c $^ -o $@ 

# clean:
# 	$(RM) *.o spilittool

# use pkg-config for getting CFLAGS and LDLIBS
FFMPEG_LIBS=    libavformat                        \
                libavcodec                         \
                libswscale                         \
                libavutil                          \

CFLAGS += -Wall -g
CFLAGS := $(shell pkg-config --cflags $(FFMPEG_LIBS)) $(CFLAGS)
LDLIBS := $(shell pkg-config --libs $(FFMPEG_LIBS)) $(LDLIBS)

EXAMPLES=       spilittool
OBJS=$(addsuffix .o,$(EXAMPLES))

# the following examples make explicit use of the math library
avcodec:           LDLIBS += -lm
muxing:            LDLIBS += -lm
resampling_audio:  LDLIBS += -lm

.phony: all clean-test clean

all: $(OBJS) $(EXAMPLES)

clean-test:
	$(RM) test*.pgm test.h264 test.mp2 test.sw test.mpg

clean: clean-test
	$(RM) $(EXAMPLES) $(OBJS)
