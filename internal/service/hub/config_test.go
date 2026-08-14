package hub

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestConfig_MapKey(t *testing.T) {
	t.Run("Success", func(t *testing.T) {
		c := NewConfig("test", "testdata/new.yml", "zqkunt22r0bewti9", "test", "PhotoPrism/Test", "test")
		assert.Equal(t, "", c.MapKey())
	})
}
